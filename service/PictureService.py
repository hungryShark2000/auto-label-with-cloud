from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import *
from model.Pictures import Picture

"""
 Connect to database and return a Session object
"""
def connectToDatabase():

    engine = create_engine("postgresql://postgres:Masha101@localhost/cloudClassification", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

"""
Edit a record based on its id, and classification given by user
return path for training use
"""
def editRecord(pathh, classification):

    session = connectToDatabase()
    record = session.query(Picture).filter_by(path=pathh).one()
    record.isClassified = True
    record.classification = classification
    session.add(record)
    session.commit()
    session.close()
    #TODO return path

def addRecord(path):
    """
    add a picture for us to classify, return its path
    """
    picture = Picture()
    picture.path = path
    picture.isClassified = False
    session = connectToDatabase()
    session.add(picture)
    session.commit()
    session.close()
    return path

def getRandomId():
    return randint(1, 8394)

#TODO add doesn't find exception
def getRandomPathRaw():
    """
    :return: random path name
    """
    session = connectToDatabase()
    result = session.query(Picture).filter_by(isClassified='False', id=getRandomId()).one()
    print(result.path)
    return result.path

def getRandomPath(rawPath):
    """
    :return: random path name
    """
    path = "database/classification-photos/"+ rawPath
    print(path)
    return path

#getRandomPath("OIP-IHAIqlTWOBVbfOzTnnz68gHaJ3.jpeg")
