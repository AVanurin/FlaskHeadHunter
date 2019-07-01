import sqlite3
from flask import g


def get_db():

    if "db" not in g:
        g.db = sqlite3.connect('generalDB.db')

    return g.db


def close_db(e=None):

    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():

    db = get_db()

    with ("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))