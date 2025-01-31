from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
import routes

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

routes.init_app(app)

@app.route('/')
def home():
    return 'Hello, Contact App!!!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)