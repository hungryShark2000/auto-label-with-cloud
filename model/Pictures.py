import csv

from dateutil.parser import parse
from sqlalchemy import Column, Integer, String, create_engine, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://postgres:Masha101@localhost/cloudClassification", echo=True)

Base = declarative_base()


class Picture(Base):
    """SQLAlchemy mapped class. Maps a Picture object to the corresponding
    database table."""

    __tablename__ = "pictures2"

    id = Column(Integer, primary_key=True)

    path = Column(String(200))
    isClassified = Column(Boolean, unique=False, default=False)
    classification = Column(String(200))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def parse_name(path):
    """inserts name"""
    return path

def parse_isClassified(isClass):
    """set to false"""
    return isClass

def parse_class(classs):
    """inserts class as none"""

    try:
        return parse(classs)
    except:
        return None

def prepare_picture(row):
    """Takes a row from CSV file and returns a Picture object from it."""

    row["path"] = parse_name(row["path"])
    row["isClassified"] = parse_name(row["isClassified"])
    row["classification"] = parse_name(row["classification"])
    return Picture(**row)


with open("../database/picturePaths.csv", encoding="utf-8", newline="") as csv_file:
    csvreader = csv.DictReader(csv_file, quotechar='"')

    pictures = [prepare_picture(row) for row in csvreader]

    session = Session()
    session.add_all(pictures)
    session.commit()