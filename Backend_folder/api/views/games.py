#!/usr/bin/python3
"""Handles RESTApi actions for games"""
from flask import abort, jsonify, request
from api.views import app_views
from models import storage
from models.games import Game
from models.user import User


@app_views.route("/games", strict_slashes=False)
def return_games():
    """Return a list of all games"""
    games = storage.all(Game)
    games_list = []
    for game in games.values():
        games_list.append(game.to_dict())
    return jsonify(games_list), 200


@app_views.route("/games/<user_id>", methods=["PUT"], strict_slashes=False)
def update_user_games(user_id):
    """Updates a user games
    Recieves a JSON with all the games in a list
    [<game_id>, <game_id2>]"""
    body = request.get_json()
    if body is None:
        abort(400, "Not a JSON")

    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    games_list = []
    games_dict = []
    for game in user.games:
        user.games.remove(game)
    storage.save()
    for game in body:
        games_list.append(storage.get(Game, game))
    for game in games_list:
        user.games.append(game)
        games_dict.append(game.to_dict()["id"])
    storage.save()
    return jsonify(games_dict), 200
