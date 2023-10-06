from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet name", validators=[InputRequired()])
    species = SelectField(
        "Pet Species",
        choices=[
            ("cat", "Cat"),
            ("dog", "Dog"),
            ("porcupine", "Porcupine")
        ],
        validators=[InputRequired()],
    )
    photo_url = StringField("Pet photo", validators=[Optional(), URL()])
    age = SelectField(
        "Pet Age",
        choices=[
            ("baby", "Baby"),
            ("young", "Young"),
            ("adult", "Adult"),
            ("senior", "Senior"),
        ],
        validators=[InputRequired()],
    )
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing pets"""

    photo_url = StringField("Pet photo", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available", validators=[Optional()])