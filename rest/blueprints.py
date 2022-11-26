from flask import Blueprint
from controller.PictureController import index, getPicturePath, insertPictureClass, indexClassify, indexSeeClassification, getUserPicture, postClass

blueprint = Blueprint('blueprint', __name__)

"""
allows users to see all possible routes
"""
blueprint.route('/', methods=['GET'])(index)

"""
Two possible function; a user can be given a picture to classify, or
the user can upload their own picture and get our classification
"""
blueprint.route('/classify', methods=['GET'])(indexClassify)
blueprint.route('/see-classification', methods=['GET'])(indexSeeClassification)

"""
User is shown a picture to classify
"""
blueprint.route('/classify/see-picture', methods=['POST'])(
    #Get path to get picture from
    path = getPicturePath
    #use path to display picture
)

"""
We get the user's classification for the picture they were given to classify, and insert it into the database, 
and use it as a training picture
"""
blueprint.route('classify/get-class', methods=['GET'])(
    #get the class from the user
    insertPictureClass
)


"""
We get the picture a user wants us to classify
"""
blueprint.route('/see-classification/get-picture', methods=['GET'])(getUserPicture)

"""
We give our classification of the picture to the user
"""
blueprint.route('see-classification/post-class', methods=['POST'])(postClass)