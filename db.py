import sqlite3
from flask import current_app
from flask import g


def get_db():

    if "db" not in g:
        g.db = sqlite3.connect('generalDB.db')
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):

    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():

    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))

