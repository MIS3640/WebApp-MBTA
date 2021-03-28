from wtforms import Form, StringField, SubmitField, validators


"""Create a form to request the place name from the user and check if it is valid"""
class GeoForm(Form):
    placename = StringField(
        "place name", [validators.DataRequired(), validators.Length(min=3, max=20)]
    )
    submit = SubmitField("Submit")
