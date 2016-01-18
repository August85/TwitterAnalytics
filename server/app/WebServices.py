import os
from flask.ext import restful
import main

HTML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../static')


class Home2(restful.Resource):
    def get(self):
        return "{'result':'true'}"

main.api.api.add_resource(Home2, "/home2")