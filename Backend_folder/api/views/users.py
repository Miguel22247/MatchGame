#!/usr/bin/python3
"""Handles RESTApi actions for users"""
from flask import abort, jsonify, request
from api.views import app_views
from models import storage
from models.user import User


@app_views.route("/user/<user_id>", strict_slashes=False)
def get_user(user_id):
    """Retrieves a user from the database"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("user/<user_id>", methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    """Deletes a user from the database"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route("/user", methods=["POST"], strict_slashes=False)
def create_user():
    """Creates a new user from a JSON
    {username: <username>, email: <user_email>, password: <user_password>}"""
    body = request.get_json()
    if body is None:
        abort(400, "Not a JSON")
    users = storage.all(User)
    for user in users:
        if user.email == body["email"]:
            return jsonify("Email already in use"), 400
    new_user = User(**body)
    new_user.save()
    user_dict = new_user.to_dict()
    return jsonify(user_dict), 201


@app_views.route("/nickname/<user_id>", methods=["PUT"], strict_slashes=False)
def change_nickname(user_id):
    """Changes the username of a user"""
    body = request.get_json()
    if body is None:
        abort (400, "Not a JSON")
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.nickname = body["nickname"]
    user.save()
    return jsonify(user.to_dict()), 200


@app_views.route("/validate_user", methods=["POST"], strict_slashes=False)
def validate_user():
    """Validates the user using email and password
    Returns the user object
    {email: <user_email>, password: <user_password>}"""
    body = request.get_json()
    if body is None:
        abort(401, "Not a JSON")
    users = storage.all(User)
    for user in users.values():
        if user.email == body["email"]:
            if user.password == body["password"]:
                return jsonify(user.to_dict()), 200
            else:
                abort(400, "Wrong password")
    abort(404, "User doesn't exist")
