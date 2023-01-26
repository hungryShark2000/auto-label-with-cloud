"""Written by Masha"""
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
