"""get random pic for user, display it"""
from service.PictureService import getRandomPathRaw, getRandomPath, editRecord, addRecord

"""
Get the picture path we want a user to classify (actual picture will be gotten in rest)
return the ID of this picture
"""
def getPicturePath():
    # get pic from database
    rawPath = getRandomPathRaw()
    path = getRandomPath(rawPath)
    return [rawPath, path]

""" 
Get user's classification for the picture based on ID, insert it into the database based 
on picture ID
"""
def insertPictureClass(id, classific):
    #edit this record in the database
    editRecord(id, classific)
    #train using the new classification

""" 
Get the picture a user wants us to classify and add it to the database
return the new picture ID
"""
def getUserPicture(path):
    addRecord(path)
    #TODO return picture path
    #TODO do I need to create a new picture path?

""" 
get our prediction for the user's picture based on ID, and post this prediction to the user.
"""
def postClass(path):
    print(path)
    #call our ai to get our prediction


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