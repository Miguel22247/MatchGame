#!/usr/bin/python3
from flask import Blueprint


app_views = Blueprint("/api", __name__)


from api.views.users import *
from api.views.games import *
from api.views.matches import *
from api.views.social_accounts import *
