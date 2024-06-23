# app/config.py
import os
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

class Config:
    SECRET_KEY = "major"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'database.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
