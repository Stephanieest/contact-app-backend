from flask import request, jsonify
from models import db, User, Contact, Favourite

def init_app(app):
    @app.route('/users', methods=['GET', 'POST'])
    def handle_users():
        if request.method == 'POST':
            data = request.get_json()
            user = User(
                username=data['username'],
                email=data['email'],
            )
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": "User created", "user": {"id": user.id, "username": user.username, "email": user.email}}), 201
        
        users = User.query.all()
        return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users]), 200
    