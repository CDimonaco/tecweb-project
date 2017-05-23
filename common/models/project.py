from bson.objectid import ObjectId
from marshmallow import Schema,fields

class Project:
    def __init__(self,name,description,createdAt,id=""):
        self.id = id
        self.name = name
        self.description = description
        self.createdAt = createdAt

    def __eq__(self, other):
        """Override del metodo __eq__ necessario per il testing."""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        """ Definisce quando due oggetti non sono uguali. Necessario per il testing"""
        return not self.__eq__(other)

    def __str__(self):
        return "<Project>: " + self.name + " " + self.description + " " + str(self.createdAt)

    @staticmethod
    def to_model(mongoproject):
        return Project(id=str(mongoproject["id"]),name=mongoproject["name"],description=mongoproject["description"],createdAt=mongoproject["createdAt"])

    @staticmethod
    def from_model(appproject):
        mongoDict = {
            "id" : ObjectId(),
            "name" : appproject.name,
            "description" : appproject.description,
            "createdAt" : appproject.createdAt
        }
        return mongoDict


class ProjectModelView(Schema):
    id = fields.String(required=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    createdAt = fields.DateTime(required=True)