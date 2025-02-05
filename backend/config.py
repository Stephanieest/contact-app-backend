import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
