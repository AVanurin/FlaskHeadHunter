from flask import render_template


def render_homepage():
    return render_template("home.html")


def render_registration_form():
    return render_template("registration_form.html")


