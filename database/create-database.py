# Create database
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy_utils import database_exists, create_database

engine = create_engine("postgresql://postgres:Masha101@localhost/cloudClassification")
if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))
