from flask import Flask

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Initialization the app application
app = Flask(__name__)

# That setting don't allows JSON displaying by the alphabet
app.config['JSON_SORT_KEYS'] = False

# Creating a binding to a DB to work with a DB
# engine = create_engine('postgresql://postgres:postgres@localhost/store')
engine = create_engine('postgres://knsdsutdhbngfy:7fef2ba41102b267640cd8f043a8a38a7fbfbc2fa647c4792e457750820c34d1@ec2-54-228-9-90.eu-west-1.compute.amazonaws.com:5432/dbd84nse1qndtl')

# Session object
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Base class object for model class
Base = declarative_base()
Base.query = session.query_property()

# DB initialization
from models import Resource

# Views initialization
from views import *
