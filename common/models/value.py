import dateutil.parser
from bson.objectid import ObjectId
class Value:
    def __init__(self,value,timestamp,sensorid,additional="",id=""):
        self.id = id
        self.value = value
        self.timestamp = timestamp
        self.additional = additional
        self.sensorid = sensorid

    def __eq__(self, other):
        """Override del metodo __eq__ necessario per il testing."""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        """ Definisce quando due oggetti non sono uguali. Necessario per il testing"""
        return not self.__eq__(other)


    def __str__(self):
        return "<Value>: "+self.id+" "+str(self.value)+" "+self.additional + " " + str(self.timestamp) + " " + self.sensorid

    @staticmethod
    def to_model(mongovalue):
        return Value(id=str(mongovalue["_id"]),value=mongovalue["value"],additional=mongovalue["additional"],timestamp=mongovalue["timestamp"],sensorid=str(mongovalue["sensorid"]))

    @staticmethod
    def from_model(appvalue):
        mongoDict = {
            "_id" : ObjectId(),
            "value" : appvalue.value,
            "additional" : appvalue.additional,
            "timestamp" : appvalue.timestamp,
            "sensorid" : ObjectId(appvalue.sensorid)
        }
        return mongoDict
