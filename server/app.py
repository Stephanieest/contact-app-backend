from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

routes.init_app(app)

@app.route('/')
def home():
    return 'Hello, Contact App!!'

if __name__ == '__main__':
    app.run(debug=True)