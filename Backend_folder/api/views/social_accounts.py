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
    social_dict = {}
    for social in socials.values():
        social_dict = social.to_dict()
        social_dict["link"] = ""
        socials_list.append(social_dict)
    return jsonify(socials_list), 200


@app_views.route("/socials/<user_id>", strict_slashes=False)
def get_user_socials(user_id):
    """Returns all social accounts of a user"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    socials_list = []
    social = {}
    for user_social in user.socials:
        social["id"] = user_social.social_id
        social["name"] = user_social.socials.to_dict()["name"]
        social["link"] = ""
        socials_list.append(social)
    return jsonify(socials_list), 200


@app_views.route("/socials/<user_id>", methods=["PUT"], strict_slashes=False)
def set_user_socials(user_id):
    """Changes the user social accounts
    {[{id: <social_id>, link: <social_link>}, {id: <social_id2>, link: <social_link2>}]}"""
    body = request.get_json()
    if body is None:
        abort(400)
    user = storage.get(User, user_id)
    if user is None:
        return jsonify("User not found"), 401
    user_socials = []
    for pair in body:
        if len(pair["link"]) == 0:
            continue
        social = storage.get(Social, pair["id"])
        if social is None:
            return jsonify("Social not found"), 402
        user_social = UserSocial(link=pair["link"])
        user_social.socials = social
        user.socials.append(user_social)
        user_social_dict = user_social.to_dict()
        user_social_dict["socials"] = user_social_dict["socials"].to_dict()
        user_socials.append(user_social_dict)

    return jsonify(user_socials), 200