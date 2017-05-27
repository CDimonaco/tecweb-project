from marshmallow import Schema,fields
from bson.objectid import ObjectId
class Sensor:
    def __init__(self,name,apikey,project,id=""):
        self.id = id
        self.name = name
        self.project = project
        self.apikey = apikey

    def __str__(self):
        return "<Sensor>: "+self.name+" "+self.id+" "+self.apikey+" "+self.project

    def __eq__(self, other):
        """Override del metodo __eq__ necessario per il testing."""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        """ Definisce quando due oggetti non sono uguali. Necessario per il testing"""
        return not self.__eq__(other)

    @staticmethod
    def to_model(mongosensor):
        return Sensor(id=str(mongosensor["_id"]),name=mongosensor["name"],apikey=mongosensor["apikey"],project=str(mongosensor["project"]))

    @staticmethod
    def from_model(appsensor):
        sensorDict = {
            "name" : appsensor.name,
            "apikey" : appsensor.apikey,
            "project" : ObjectId(appsensor.project),
        }
        return sensorDict


class SensorViewModel(Schema):
    id = fields.String(required=True)
    name = fields.String(required=True)
    apikey = fields.String(required=True)
