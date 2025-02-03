from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Contact(db.Model):
    __tablename__ = 'contact'  # Added tablename here
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'user_id': self.user_id
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'  # Added tablename here
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)
    starred = db.Column(db.Boolean, default=False)

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'contact_id': self.contact_id,
            'starred': self.starred
        }
