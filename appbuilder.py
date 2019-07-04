from flask import Flask
from flask import request
import sqlite3
from flask import g


class AppBuilder:
    def __init__(self):
        pass

    def build(self):
        app = Flask(__name__)

        @app.route("/login", methods=['GET'])
        def login():
            pass

        @app.route("/login", methods=['POST'])
        def add_new_users():
            if request.form['login', 'password', 'email'] == '':
                return "Error"
            else:
                def get_db():
                    if "db" not in g:
                        g.db = sqlite3.connect('generalDB.db')
                    return g.db

                db = get_db()

                with "SelectDB.sql" as f:
                    db.executescript(f.read().decode("utf8"))

        return app


