from flask import  Flask
from Resourses import web_controllers as wc
from flask import request

class AppBuilder:
    def __init__(self):
        pass

    def build(self):
        app = Flask(__name__)

        @app.route("/")
        @app.route("/home")
        def go_to_home():
            return wc.render_homepage()

        @app.route('/registration', metod=['GET'])
        def go_to_registration():
            return wc.render_registration_form()



        return app
