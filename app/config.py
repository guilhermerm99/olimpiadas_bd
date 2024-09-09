import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma-chave-secreta'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://root:grdm9977@localhost/olimpiadasdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
