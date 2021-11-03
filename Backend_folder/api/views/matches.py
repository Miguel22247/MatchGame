#!/usr/bin/python3.6
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
        storage.save()
        return jsonify("Match"), 201
    elif user in like.matches:
        return jsonify("Already a match"), 201
    else:
        user.likes.append(like)
        storage.save()
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
    """Gets all users that share at least one game with the user"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if len(user.games) is 0:
        return jsonify("Add some games in Config"), 201
    users = storage.all(User).values()
    users_list = []
    for game in user.games:
        for usr in users:
            if game in usr.games and usr not in users_list and usr not in user.likes and usr not in user.matches and usr is not user:
                users_list.append(usr)
    users_dicts = []
    for usr in users_list:
        usr_dict = usr.to_dict()
        usr_dict.pop('password')
        games_dicts = []
        for game in usr.games:
            games_dicts.append(game.to_dict())
        usr_dict["games"] = games_dicts
        users_dicts.append(usr_dict)
    return jsonify(users_dicts), 200


@app_views.route("/get_matches/<user_id>", strict_slashes=False)
def get_matches(user_id):
    """Returns all matches from a user"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    matches_list = []
    for usr in user.matches:
        usr_dict = usr.to_dict()
        games_list = []
        for game in usr.games:
            games_list.append(game.to_dict())
        usr_dict["games"] = games_list
        socials_list = []
        for user_social in usr.socials:
            user_social_dict = {}
            user_social_dict["name"] = user_social.socials.name
            user_social_dict["link"] = user_social.link
            socials_list.append(user_social_dict)
        usr_dict["socials"] = socials_list
        matches_list.append(usr_dict)
    return jsonify(matches_list)