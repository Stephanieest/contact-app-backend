from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Use(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    contacts = db.relationship('Contact', backref='user', lazy=True)
    favourites = db.relationship('Favourite', backref-'user', lazy=True)

