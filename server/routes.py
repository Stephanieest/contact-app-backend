from flask import request, jsonify
from models import db, User, Contact, Favorite

def init_app(app):
    # User CRUD
    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        user = User(username=data['username'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created", "user": user.to_dict()}), 201

    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        return jsonify([user.to_dict() for user in users]), 200

    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404
        return jsonify(user.to_dict()), 200

    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404
        data = request.get_json()
        user.username = data['username']
        user.email = data['email']
        db.session.commit()
        return jsonify({"message": "User updated", "user": user.to_dict()}), 200

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200

    # Contact CRUD
    @app.route('/contacts', methods=['POST'])
    def create_contact():
        data = request.get_json()
        contact = Contact(name=data['name'], phone=data['phone'], email=data['email'], address=data.get('address'), user_id=data['user_id'])
        db.session.add(contact)
        db.session.commit()
        return jsonify({"message": "Contact created", "contact": contact.to_dict()}), 201

    @app.route('/contacts', methods=['GET'])
    def get_contacts():
        contacts = Contact.query.all()
        return jsonify([contact.to_dict() for contact in contacts]), 200

    @app.route('/contacts/<int:contact_id>', methods=['GET'])
    def get_contact(contact_id):
        contact = Contact.query.get(contact_id)
        if not contact:
            return jsonify({"message": "Contact not found"}), 404
        return jsonify(contact.to_dict()), 200

    @app.route('/contacts/<int:contact_id>', methods=['PUT'])
    def update_contact(contact_id):
        contact = Contact.query.get(contact_id)
        if not contact:
            return jsonify({"message": "Contact not found"}), 404
        data = request.get_json()
        contact.name = data['name']
        contact.phone = data['phone']
        contact.email = data['email']
        contact.address = data.get('address')
        contact.user_id = data['user_id']
        db.session.commit()
        return jsonify({"message": "Contact updated", "contact": contact.to_dict()}), 200

    @app.route('/contacts/<int:contact_id>', methods=['DELETE'])
    def delete_contact(contact_id):
        contact = Contact.query.get(contact_id)
        if not contact:
            return jsonify({"message": "Contact not found"}), 404
        db.session.delete(contact)
        db.session.commit()
        return jsonify({"message": "Contact deleted"}), 200

    # Favorite CRUD
    @app.route('/favorites', methods=['POST'])
    def create_favorite():
        data = request.get_json()
        favorite = Favorite(user_id=data['user_id'], contact_id=data['contact_id'])
        db.session.add(favorite)
        db.session.commit()
        return jsonify({"message": "Favorite created", "favorite": favorite.to_dict()}), 201

    @app.route('/favorites', methods=['GET'])
    def get_favorites():
        favorites = Favorite.query.all()
        return jsonify([favorite.to_dict() for favorite in favorites]), 200

    @app.route('/favorites/<int:favorite_id>', methods=['GET'])
    def get_favorite(favorite_id):
        favorite = Favorite.query.get(favorite_id)
        if not favorite:
            return jsonify({"message": "Favorite not found"}), 404
        return jsonify(favorite.to_dict()), 200

    @app.route('/favorites/<int:favorite_id>', methods=['PUT'])
    def update_favorite(favorite_id):
        favorite = Favorite.query.get(favorite_id)
        if not favorite:
            return jsonify({"message": "Favorite not found"}), 404
        data = request.get_json()
        favorite.user_id = data['user_id']
        favorite.contact_id = data['contact_id']
        db.session.commit()
        return jsonify({"message": "Favorite updated", "favorite": favorite.to_dict()}), 200

    @app.route('/favorites/<int:favorite_id>', methods=['DELETE'])
    def delete_favorite(favorite_id):
        favorite = Favorite.query.get(favorite_id)
        if not favorite:
            return jsonify({"message": "Favorite not found"}), 404
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({"message": "Favorite deleted"}), 200