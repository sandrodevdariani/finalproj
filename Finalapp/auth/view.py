from flask import Blueprint, request, redirect, url_for, session, render_template
from app import db
from .model import User
import random


auth = Blueprint("auth", __name__, template_folder="templates")





    







@auth.route("/login", methods=["GET","POST"])
def login_page():
    error_msg = ""
    method = request.method
    if method == "POST":
        email = request.form.get("email", None)
        password = request.form.get("password", None)
        if email and password:
            user = User.query.filter_by(email=email).first()
            user = user.serilize()
        
            if user.get("password") == password:
                session["is_login"] = True
                session["user_name"] = user.get("name")
                return render_template('home.html')
            elif user.get("password") != password:
                error_msg = "Invalid User"
                return render_template('login.html', error_msg = error_msg)   

            else:
                error_msg = "Invalid User"
                render_template('login.html', error_msg = error_msg)
        else:
            error_msg = "Must Fill Out All Field"    
            return render_template('login.html', error_msg = error_msg)
    return render_template('login.html', error_msg = '')

@auth.route("/logout")    
def logout_page(): 
     session["is_login"] = False
     return redirect(url_for("auth.login_page"))

@auth.route("/registration", methods=["GET", "POST"])
def registration_page():
    method = request.method
    error_msg = ""
    if method == "POST":
        error_msg = "Fill All Field"
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        password = request.form.get("password")
        favinfo = request.form.get("favinfo", "")
        if name == "":
            error_msg = "Must Fill Out All Field"
            return render_template("registration.html", error_msg=error_msg)
        elif email == "":
            error_msg = "Must Fill Out All Field"
            return render_template("registration.html", error_msg=error_msg) 
        elif password == "":
            error_msg = "Must Fill Out All Field"
            return render_template("registration.html", error_msg=error_msg)
        elif favinfo == "":
            error_msg = "Must Fill Out All Field"
            return render_template("registration.html", error_msg=error_msg)
        elif len(password) < 6:
            error_msg = "Password Too Short"  
            return render_template("registration.html", error_msg=error_msg)

        try:
            user_model = User(name, email, password, favinfo)
            db.session.add(user_model)
            db.session.commit()
            return redirect(url_for("auth.login_page"))
        except Exception as e:
            return "server error"

    
    return render_template('registration.html')

@auth.route("/AboutUs")    
def AboutUs_page():
    return render_template('aboutus.html')