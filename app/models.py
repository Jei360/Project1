from . import db

class UserProfile(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(255))
    photoname = db.Column(db.String(80), unique=True)
    date = db.Column(db.String(80))
    
    def __init__(self, firstname, lastname, gender, email, location, biography, date, photoname):
        self.firstname=firstname
        self.lastname=lastname
        self.gender=gender
        self.email=email
        self.location=location
        self.biography=biography
        self.date=date
        self.photoname=photoname