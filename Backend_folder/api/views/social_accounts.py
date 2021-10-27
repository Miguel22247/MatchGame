#!/usr/bin/python3
"""Handles RESTApi actions for social accounts"""
from flask import abort, jsonify, request
from api.views import app_views
from models import storage
from models.user import User, UserSocial
from models.socials import Social


@app_views.route("/socials", strict_slashes=False)
def get_socials():
    """Returns all social networks"""
    socials = storage.all(Social)
    socials_list = []
    for social in socials.values():
        socials_list.append(social.to_dict())
    return jsonify(socials_list), 200


@app_views.route("/socials/<user_id>", strict_slashes=False)
def get_user_socials(user_id):
    """Returns all social accounts of a user"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user_dict = user.to_dict()
    return jsonify(user_dict["socials"]), 200


@app_views.route("/socials", methods=["PUT"], strict_slashes=False)
def set_user_socials():
    """Changes the user social accounts
    {user: <user_id>, social: <social_id>, link: <social_link>}"""
    body = request.get_json()
    if body is None:
        abort(400)
    user = storage.get(User, body["user"])
    if user is None:
        abort(404, "User not found")
    social = storage.get(Social, body["social"])
    if social is None:
        abort(404)
    user_social = UserSocial(link=body["link"])
    user.socials.append(user_social)
    return jsonify(user.socials), 201