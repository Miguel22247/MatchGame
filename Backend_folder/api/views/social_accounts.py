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


@app_views.route("/socials/<user_id>", methods=["PUT"], strict_slashes=False)
def set_user_socials(user_id):
    """Changes the user social accounts
    {[{social: <social_id>, link: <social_link>}, {social: <social_id2>, link: <social_link2>}]}"""
    body = request.get_json()
    if body is None:
        abort(400)
    user = storage.get(User, user_id)
    if user is None:
        abort(404, "User not found")
    user_socials = []
    for pair in body:
        social = storage.get(Social, pair["social"])
        if social is None:
            abort(404, "Social not found")
        user_social = UserSocial(link=pair["link"])
        user_socials.append(user_social)
    user.socials = user_socials
    return jsonify(user.socials), 201