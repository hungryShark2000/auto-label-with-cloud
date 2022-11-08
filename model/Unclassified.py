from flask_sqlalchemy import SQLAlchemy

#import database
#db = SQLAlchemy()


#houses unclassified pictures
class Unclassified:#(db.Model):
    varr = 1
    # __tablename__ = 'unclassified-pictures'
    #
    # id = db.Column(db.Integer, primary_key=True)
    # picture = db.Column(db.String) #this will be the picture, but for now its a string
    #
    # @property
    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'name': self.picture,
    #     }