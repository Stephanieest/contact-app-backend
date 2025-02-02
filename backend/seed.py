from app import app, db
from models import User, Contact, Favorite

with app.app_context():
    # Create all tables
    db.create_all()

    # Check if the user already exists
    existing_user = User.query.filter_by(username='user1').first()

    if not existing_user:
        # Add sample data
        user1 = User(username='user1', email='user1@example.com')
        db.session.add(user1)
        db.session.commit()  # Commit the user first so it gets an ID
    else:
        user1 = existing_user

    contact1 = Contact(name='John Doe', phone='123-456-7890', email='john.doe@example.com', address='123 Main St', user_id=user1.id)
    db.session.add(contact1)
    db.session.commit()  # Commit the contact

    favorite1 = Favorite(user_id=user1.id, contact_id=contact1.id)
    db.session.add(favorite1)
    db.session.commit()  # Commit the favorite

    print("Database seeded!")