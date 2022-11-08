import json
#from model.Unclassified import Inserttable, db
from service.user_service import show_picture, get_class


def index():
    return {'status': 'OK',
            'localhost:5000/pictures/classify': 'allow user to classify a picture',
            'localhost:5000/pictures/see-classification': 'allow user to see our classification of their picture',
            }

def indexClassify():
    return {'status': 'OK',
            'localhost:5000/pictures/classify/see-picture': 'post picture',
            'localhost:5000/pictures/classify/get-class': 'get class user assigns',
            }

def indexSeeClassification():
    return {'status': 'OK',
            'localhost:5000/pictures/see-classification/upload-picture': 'user posts picture',
            'localhost:5000/pictures/see-classification/see-classification': 'user sees how we classified it',
            }

def seePic():
    show_picture()

def getClass():
    get_class()