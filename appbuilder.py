from flask import  Flask


class AppBuilder:
    def __init__(self):
        pass

    def build(self):
        app = Flask(__name__)

        return app
