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
engine = create_engine('postgresql://postgres:postgres@localhost/store')

# Session object
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Base class object for model class
Base = declarative_base()
Base.query = session.query_property()

# DB initialization
from models import Resource

# Views initialization
from views import *
