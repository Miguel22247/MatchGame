#!/usr/bin/python3
"""Handles RESTApi actions for matches system"""
from flask import abort, jsonify, request
from api.views import app_views
from models import storage
from models.user import User


@app_views.route("/add_like", methods=["POST"], strict_slashes=False)
def add_like():
    """Add a like from a user
    {user: <user_id>, like: <user_id>}"""
    body = request.get_json()
    if body is None:
        abort(400, "Not a JSON")
    user = storage.get(User, body["user"])
    if user is None:
        abort(404)
    like = storage.get(User, body["like"])
    if like is None:
        abort(404)
    if user in like.likes:
        like.likes.remove(user)
        like.matches.append(user)
        user.matches.append(like)
        return jsonify("Match"), 200
    else:
        user.likes.append(like.id)
        return jsonify("Like"), 200


@app_views.route("/delete_match", methods=["DELETE"], strict_slashes=False)
def delete_match():
    """Deletes a match from a user
    {user: <user_id>, match: <match_id>}"""
    body = request.get_json()
    if body is None:
        abort(400, "Not a JSON")
    user = storage.get(User, body["user"])
    if user is None:
        abort(404)
    match = storage.get(User, body["match"])
    if match is None:
        abort(404)
    if match in user.matches:
        user.matches.remove(match)
    if user in match.matches:
        match.matches.remove(user)
    return jsonify("Deleted"), 200


@app_views.route("/get_users/<user_id>", strict_slashes=False)
def get_users(user_id):
    """Gets a user to display"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if len(user.games) is 0:
        return jsonify("Add some games in Config"), 201
    users = storage.all(User)
    users_list = []
    for game in user.games:
        for usr in users:
            if game in usr.games and usr not in users_list:
                users_list.append(usr)
    users = []
    for usr in users_list:
        usr_dict = usr.to_dict()
        usr_dict.pop('password')
        users.append(usr_dict)
    return jsonify(users), 200


#@app_views.route("/get_matches/<user_id>", strict_slashes=False)
#def get_matches(user_id):