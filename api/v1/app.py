#!/usr/bin/python3
""" this module starts a flask app """
import os
from flask import Flask, make_response, jsonify
from models import storage
from api.vi.views import app_views
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def remove(exception):
    """ deletes the current session """
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """ handles 404 error response """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    environ_host = os.getenv("HBNB_API_HOST")
    environ_port = os.getenv("HBNB_API_PORT")

    app.run(host=environ_host if environ_host else "0.0.0.0"),
    port=environ_port if environ_port else 5000,
    threaded=True
