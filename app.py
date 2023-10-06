import os
from flask import Flask, render_template, redirect, request, flash
from forms import AddPetForm, EditPetForm
from models import db, connect_db, Pet
from petfinder import update_auth_token_string, get_random_animal
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "postgresql:///pets"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)


app.config["SECRET_KEY"] = 'shhhhhhhhh'

debug = DebugToolbarExtension(app)


@app.get("/")
def home():
    #TODO: rename more descriptively and do docstring better
    """Returns home page."""

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Displays add pet form; handle adding"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data #TODO: remove

        pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes,
            available=available)

        db.session.add(pet)
        db.session.commit()

        flash("Pet successfully added!")

        return redirect("/")

    return render_template("add_pet.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def display_and_edit_pet(pet_id):
    """Displays pet info and editable information of that pet"""

    pet = Pet.query.get_or_404(pet_id)

    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available

        db.session.commit()

        flash("Pet successfully updated!")

        return redirect("/")

    return render_template("edit_pet.html", form=form, pet=pet)