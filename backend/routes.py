from flask import request, jsonify
from models import db, User, Contact, Favorite

def init_app(app):
    # User Routes
    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        return jsonify([user.serialize() for user in users])

    @app.route('/users', methods=['POST'])
    def add_user():
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.serialize()), 201

    @app.route('/users/<int:id>', methods=['PUT'])
    def update_user(id):
        data = request.get_json()
        user = User.query.get(id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        user.username = data['username']
        user.email = data['email']
        db.session.commit()
        return jsonify(user.serialize())

    @app.route('/users/<int:id>', methods=['DELETE'])
    def delete_user(id):
        user = User.query.get(id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        db.session.delete(user)
        db.session.commit()
        return '', 204

    # Contact Routes
    @app.route('/contacts', methods=['GET'])
    def get_contacts():
        contacts = Contact.query.all()
        return jsonify([contact.serialize() for contact in contacts])

    @app.route('/contacts', methods=['POST'])
    def add_contact():
        data = request.get_json()
        new_contact = Contact(name=data['name'], phone=data['phone'], email=data['email'], address=data.get('address'), user_id=data['user_id'])
        db.session.add(new_contact)
        db.session.commit()
        return jsonify(new_contact.serialize()), 201

    @app.route('/contacts/<int:id>', methods=['PUT'])
    def update_contact(id):
        data = request.get_json()
        contact = Contact.query.get(id)
        if not contact:
            return jsonify({'error': 'Contact not found'}), 404
        contact.name = data['name']
        contact.phone = data['phone']
        contact.email = data['email']
        contact.address = data.get('address')
        contact.user_id = data['user_id']
        db.session.commit()
        return jsonify(contact.serialize())

    @app.route('/contacts/<int:id>', methods=['DELETE'])
    def delete_contact(id):
        contact = Contact.query.get(id)
        if not contact:
            return jsonify({'error': 'Contact not found'}), 404
        db.session.delete(contact)
        db.session.commit()
        return '', 204

    # Favorite Routes
    @app.route('/favorites', methods=['GET'])
    def get_favorites():
        favorites = Favorite.query.all()
        return jsonify([favorite.serialize() for favorite in favorites])

    @app.route('/favorites', methods=['POST'])
    def add_favorite():
        data = request.get_json()
        new_favorite = Favorite(user_id=data['user_id'], contact_id=data['contact_id'])
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify(new_favorite.serialize()), 201

    @app.route('/favorites/<int:id>', methods=['PUT'])
    def update_favorite(id):
        data = request.get_json()
        favorite = Favorite.query.get(id)
        if not favorite:
            return jsonify({'error': 'Favorite not found'}), 404
        favorite.user_id = data['user_id']
        favorite.contact_id = data['contact_id']
        favorite.starred = data['starred']
        db.session.commit()
        return jsonify(favorite.serialize())

    @app.route('/favorites/<int:id>', methods=['DELETE'])
    def delete_favorite(id):
        favorite = Favorite.query.get(id)
        if not favorite:
            return jsonify({'error': 'Favorite not found'}), 404
        db.session.delete(favorite)
        db.session.commit()
        return '', 204