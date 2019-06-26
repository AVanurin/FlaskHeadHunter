from flask import  Flask
from Resourses import web_controllers as wc


class AppBuilder:
    def __init__(self):
        pass

    def build(self):
        app = Flask(__name__)

        @app.route("/")
        @app.route("/home")
        def go_to_home():
            return wc.render_homepage()

        return app
