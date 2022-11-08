from flask import Blueprint
from controller.UserClassifies import index, seePic, getClass, indexClassify, indexSeeClassification

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/classify', methods=['GET'])(indexClassify)
blueprint.route('/see-classification', methods=['GET'])(indexSeeClassification)

blueprint.route('/classify/see-picture', methods=['POST'])(seePic)
blueprint.route('classify/get-class', methods=['GET'])(getClass)