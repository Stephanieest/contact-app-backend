from app import app, db
from models import User, Contact, Favorite
from faker import Faker

fake = Faker()

with app.app_context():
    # Create all tables if they don't already exist
    db.create_all()

    users = {}
    
    # Create 20 users
    for _ in range(20):  
        username = fake.unique.user_name()  # Ensure the username is unique

        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        
        if not existing_user:
            # Create a new user if not existing
            user = User(username=username, email=f'{username}@example.com')
            db.session.add(user)
            try:
                db.session.commit()  # Commit after adding the user
                print(f"Added user: {username}")
                users[username] = user
            except Exception as e:
                db.session.rollback()
                print(f"Error adding user {username}: {e}")
        else:
            # Use existing user if already in database
            print(f"User {username} already exists, skipping.")
            users[username] = existing_user

    # Add contacts and favorites for each user
    for username, user in users.items():
        for _ in range(3):  # Add 3 contacts per user
            contact = Contact(
                name=fake.name(),
                phone=fake.phone_number(),
                email=fake.unique.email(),  # Ensure unique emails for contacts
                address=fake.address(),
                user_id=user.id
            )
            db.session.add(contact)
            
            # Create a favorite entry for the user and the contact
            favorite = Favorite(user_id=user.id, contact_id=contact.id)
            db.session.add(favorite)

        # Commit once after adding all contacts and favorites for a user
        try:
            db.session.commit()
            print(f"Added contacts and favorites for {username}")
        except Exception as e:
            db.session.rollback()
            print(f"Error adding contacts and favorites for {username}: {e}")

    print("Database seeded successfully!")
