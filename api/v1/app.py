#!/usr/bin/python3
"""
the main module of the app
"""
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exc):
    """ hanle teardown_qppcontext """
    storage.close()


<<<<<<< HEAD
=======
@app.errorhandler(404)
def not_found(error):
    """ handler for 404 errors """
    return make_response(jsonify({'error': 'Not found'}), 404)

>>>>>>> 96a34c5a7cdd53268d983c7602a138306c49f834

if __name__ == "__main__":
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')
    if HBNB_API_HOST is None:
        HBNB_API_HOST = '0.0.0.0'
    if HBNB_API_PORT is None:
        HBNB_API_PORT = '5000'
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
