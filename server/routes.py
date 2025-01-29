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
    
    @app.route('api/contacts', methods=['GET', 'POST'])
    def handle_contacts():
        if request.method == 'POST':
            data = request.get_json()
            contact = Contact(
                name=data['name'],
                phone=data['phone'],
                email=data['email'],
                address=data['address'],
                user_id=data['user_id'],
            )
            db.session.add(contact)
            db.session.commit()
            return jsonify({"message": "Contact created", "contact": contact.to_dict()}), 201
        
        contacts = Contact.query.all()
        return jsonify([contact.to_dict() for contact in contacts]), 200
    
    @app.route('/api/contacts/<int:contact_id>', methods=['GET', 'PUT', 'DELETE'])
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
        
     @app.route('/api/favourites', methods=['GET', 'POST'])
    def handle_favourites():
        if request.method == 'POST':
            data = request.get_json()
            favourite = Favourite(
                user_id=data['user_id'],
                contact_id=data['contact_id']
            )
            db.session.add(favourite)
            db.session.commit()
            return jsonify({"message": "Favourite created", "favourite": favourite.to_dict()}), 201

        favourites = Favourite.query.all()
        return jsonify([favourite.to_dict() for favourite in favourites]), 200

    @app.route('/api/favourites/<int:favourite_id>', methods=['GET', 'PUT', 'DELETE'])
    def handle_favourite(favourite_id):
        favourite = Favourite.query.get(favourite_id)
        if not favourite:
            return jsonify({"message": "Favourite not found"}), 404

        if request.method == 'GET':
            return jsonify(favourite.to_dict()), 200

        if request.method == 'PUT':
            data = request.get_json()
            favourite.user_id = data['user_id']
            favourite.contact_id = data['contact_id']
            db.session.commit()
            return jsonify({"message": "Favourite updated", "favourite": favourite.to_dict()}), 200

        if request.method == 'DELETE':
            db.session.delete(favourite)
            db.session.commit()
            return jsonify({"message": "Favourite deleted"}), 200