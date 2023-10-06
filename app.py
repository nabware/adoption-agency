import os
from flask import Flask, render_template, redirect, request, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///pets')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)


@app.get("/")
def home():
    """Return home page."""

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)