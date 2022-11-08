# from flask_sqlalchemy import SQLAlchemy
#
# #import database
# db = SQLAlchemy
#
# #houses pictures with their classification user provided
# class UserClassified(db.Model):
#     __tablename__ = 'unclassified-pictures'
#
#     id = db.Column(db.Integer, primary_key=True)
#     picture = db.Column(db.String) #this will be the picture, but for now its a string
#     classification = db.Column(db.String)
#
#     @property
#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.picture,
#             'classification': self.classification
#         }