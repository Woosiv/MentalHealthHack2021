import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ''' Setup Flask configuration with environment variables '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APIKEY = os.environ.get('APIKEY')