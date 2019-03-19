from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired, DataRequired, Email

class SignupForm(FlaskForm):
    firstname= StringField('firstname', validators=[InputRequired()])
    lastname=StringField('lastname', validators=[InputRequired()])
    gender=StringField('gender', validators=[InputRequired()])
    email=StringField('email', validators=[InputRequired(), Email()])
    location=StringField('location', validators=[InputRequired()])
    biography=StringField('biography', validators=[InputRequired()])
    file= FileField('form', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])