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
    user_dict = user.to_dict()
    user_dict.pop('password')
    user_games = []
    for game in user.games:
        user_games.append(game.to_dict()["id"])
    user_dict["games"] = user_games
    return jsonify(user_dict), 200


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
    for user in users.values():
        if user.email == body["email"]:
            return jsonify("Email already in use"), 400
    new_user = User(**body)
    new_user.save()
    user_dict = new_user.to_dict()
    return jsonify(user_dict), 201


@app_views.route("/bio/<user_id>", methods=["PUT"], strict_slashes=False)
def change_username(user_id):
    """Changes the username of a user
    {username: <new_username>, bio: <new_bio>"""
    body = request.get_json()
    if body is None:
        abort (400, "Not a JSON")
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.username = body["username"]
    user.bio = body["bio"]
    games_list =[]
    for game in user.games:
        games_list.append(game.to_dict())
    user_dict = user.to_dict()
    user_dict["games"] = games_list
    user.save()
    return jsonify(user_dict), 200


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
