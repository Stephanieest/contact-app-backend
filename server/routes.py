from flask import request, jsonify
from models import db, User, Contact, Favorite

def init_app(app):
    @app.route('/users', methods=['GET', 'POST'])
    def handle_users():
        if request.method == 'POST':
            data = request.get_json()
            user = User(
                username=data['username'],
                email=data['email']
            )
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": "User created", "user": {"id": user.id, "username": user.username, "email": user.email}}), 201

        users = User.query.all()
        return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users]), 200

    @app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
    def handle_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404

        if request.method == 'GET':
            return jsonify({"id": user.id, "username": user.username, "email": user.email}), 200

        if request.method == 'PUT':
            data = request.get_json()
            user.username = data['username']
            user.email = data['email']
            db.session.commit()
            return jsonify({"message": "User updated", "user": {"id": user.id, "username": user.username, "email": user.email}}), 200

        if request.method == 'DELETE':
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User deleted"}), 200

    
    @app.route('/contacts', methods=['GET', 'POST'])
    def handle_contacts():
        if request.method == 'POST':
            data = request.get_json()
            contact = Contact(
                name=data['name'],
                phone=data['phone'],
                email=data['email'],
                address=data.get('address'),
                user_id=data['user_id']
            )
            db.session.add(contact)
            db.session.commit()
            return jsonify({"message": "Contact created", "contact": contact.to_dict()}), 201

        contacts = Contact.query.all()
        return jsonify([contact.to_dict() for contact in contacts]), 200

    @app.route('/contacts/<int:contact_id>', methods=['GET', 'PUT', 'DELETE'])
    def handle_contact(contact_id):
        contact = Contact.query.get(contact_id)
        if not contact:
            return jsonify({"message": "Contact not found"}), 404

        if request.method == 'GET':
            return jsonify(contact.to_dict()), 200

        if request.method == 'PUT':
            data = request.get_json()
            contact.name = data['name']
            contact.phone = data['phone']
            contact.email = data['email']
            contact.address = data.get('address')
            contact.user_id = data['user_id']
            db.session.commit()
            return jsonify({"message": "Contact updated", "contact": contact.to_dict()}), 200

        if request.method == 'DELETE':
            db.session.delete(contact)
            db.session.commit()
            return jsonify({"message": "Contact deleted"}), 200

    
    @app.route('/favorites', methods=['GET', 'POST'])
    def handle_favorites():
        if request.method == 'POST':
            data = request.get_json()
            favorite = Favorite(
                user_id=data['user_id'],
                contact_id=data['contact_id']
            )
            db.session.add(favorite)
            db.session.commit()
            return jsonify({"message": "Favorite created", "favorite": favorite.to_dict()}), 201

        favorites = Favorite.query.all()
        return jsonify([favorite.to_dict() for favorite in favorites]), 200

    @app.route('/favorites/<int:favorite_id>', methods=['GET', 'PUT', 'DELETE'])
    def handle_favorite(favorite_id):
        favorite = Favorite.query.get(favorite_id)
        if not favorite:
            return jsonify({"message": "Favorite not found"}), 404

        if request.method == 'GET':
            return jsonify(favorite.to_dict()), 200

        if request.method == 'PUT':
            data = request.get_json()
            favorite.user_id = data['user_id']
            favorite.contact_id = data['contact_id']
            db.session.commit()
            return jsonify({"message": "Favorite updated", "favorite": favorite.to_dict()}), 200

        if request.method == 'DELETE':
            db.session.delete(favorite)
            db.session.commit()
            return jsonify({"message": "Favorite deleted"}), 200