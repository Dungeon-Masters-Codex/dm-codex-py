# TODO: I don't want myself or anyone to have to deal with pgadmin, container anyone?

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# TODO: find a simple cloud postgress to get serve as the db and get the url from that
# I botched the local setup in frustration to get this off the ground and have spent far too much time on it

DATABASE_URL = 'fixmewithcloudurl'