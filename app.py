from flask import Flask, render_template, redirect, request, url_for, session
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)







app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://edrmtzkiuflmff:4e2d4f3844a192438dfc1f072ad10b78e056cadfd78ebb03d774554102bfb0d7@ec2-54-166-107-5.compute-1.amazonaws.com:5432/d63matt9ih2k7k"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(12)
db = SQLAlchemy(app)




from Finalapp.auth.view import auth

from Finalapp.auth.model import User
app.register_blueprint(auth, url_prefix="/auth")







@app.route("/")
def index():
    is_login = session.get("is_login", False)
    if is_login == True:
        return render_template("home.html")
    else:
        return render_template("login.html")

@app.route("/home")        
def home():
    is_login = session.get("is login", False)
    if is_login == True:
        return render_template("home.html")
    else:
        return render_template("home.html") 


 
   
    
  
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    
    app.run
    