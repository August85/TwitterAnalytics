import os
from flask import Flask
from flask import send_from_directory
from flask.ext import restful

ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/app')
HTML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


app = Flask(__name__, template_folder=ASSETS_DIR, static_folder=ASSETS_DIR)

# flask-restful
api = restful.Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Content-Disposition')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


class Home(restful.Resource):
    def get(self):
        return send_from_directory(HTML_DIR, 'index.html')

api.add_resource(Home, '/')


