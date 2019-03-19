import os
from datetime import datetime
from app import app, db
from app.models import UserProfile
from flask import render_template, request, url_for, redirect, flash
from werkzeug.utils import secure_filename
from app.forms import SignupForm


@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/about')
def about():
    return render_template('home.html')

@app.route('/profile', methods=["POST", "GET"])
def profile():
    myform=SignupForm()
    if request.method=="POST":
        if myform.validate_on_submit():
            first=myform.firstname.data
            last=myform.lastname.data
            gen=myform.gender.data
            email=myform.email.data
            loc=myform.location.data
            bio=myform.biography.data
            pic= request.files['file']
            now = datetime.now()
            signdate=  now.strftime("%B")+" "+str(now.day)+", "+str(now.year)
            photoname=secure_filename(pic.filename)
            pic.save(os.path.join(app.config['UPLOAD_FOLDER'], photoname))
            
            user= UserProfile(first, last, gen, email, loc, bio, signdate, photoname)
            db.session.add(user)
            db.session.commit()
            
            flash("Profile Successfully Created", "success")
            return redirect("/")
        else:
            flash("Failed to create profile", "danger")
    return render_template('profile.html', myform=myform)

@app.route('/profiles')
def profiles():
    users = db.session.query(UserProfile).all()
    return render_template('profiles.html', users=users)
    
@app.route('/profile/<userid>')
def aprofile(userid):
     user=db.session.query(UserProfile).get("{0}".format(userid))
     return render_template("aprofile.html", user=user)
