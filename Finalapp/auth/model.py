from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=True)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    favinfo = db.Column(db.String(), nullable=False)
    

    created_on = db.Column(db.DateTime(), default=datetime.now)
    uptaded_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)


    def __init__(self, name, email, password, favinfo):
        self.name = name
        self.email = email
        self.password = password
        self.favinfo = favinfo
       

   

    def __repr__(self):
        return'<id {}>'.format(self.id)

    def serilize(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "favinfo": self.favinfo
        }    


    