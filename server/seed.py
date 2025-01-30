from app import app, db
from models import User, Contact, Favorite

with app.app_context():
    db.create_all()

    # Add initial data
    user1 = User(username='user1', email='user1@example.com')
    contact1 = Contact(name='John Doe', phone='1234567890', email='john@example.com', address='123 Main St', user_id=user1.id)
    favorite1 = Favorite(user_id=user1.id, contact_id=contact1.id)

    db.session.add(user1)
    db.session.add(contact1)
    db.session.add(favorite1)

    db.session.commit()