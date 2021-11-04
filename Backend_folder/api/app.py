#!/usr/bin/python3.6
"""Creates an instance of Flask"""
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api")
CORS(app, resources={r"/*": {"origins": "*"}})


@app.teardown_appcontext
def close_session(self):
    """Closes the storage session"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """Handles a page not found error"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", threaded=True)