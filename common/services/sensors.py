from common.settings import persistenceSettings
from common.models.sensor import Sensor
from common.exceptions.sensors import SensorAddError,SensorNotFoundError
from common.models.value import Value
from bson.objectid import ObjectId
from common.exceptions.values import ValueAddError,ValueNotFoundError

class SensorService:
    def __init__(self,database):
        self.collection = database[persistenceSettings["sensorsCollection"]]


    def getAll(self):
        """
        Metodo di test, ritorna tutti i sensori e li stampa a schermo.
        :return: 
        """
        sensorcursor = self.collection.find()
        sensorlist = [user for user in sensorcursor]
        testsensors = {"count": sensorcursor.count(), "users": sensorlist}
        print(testsensors)

    def add(self,sensor):
        sensortoadd = Sensor.from_model(sensor)
        insertionResult = self.collection.insert_one(sensortoadd)
        if not insertionResult.acknowledged:
            raise SensorAddError
        print("Insertion completed", insertionResult.inserted_id)
        return insertionResult.inserted_id

    def delete(self,filter):
        """
        Questo metodo elimina dei sensori dalla collezione secondo i filtri in input.
        :param filter: SensorFilter
        :return: True
        """
        deleteResult = self.collection.delete_many(filter.getConditions())
        if deleteResult.deleted_count < 1:
            # TODO:ADD LOG TO FLASK
            raise SensorNotFoundError
        return True

    def find(self,filter):
        """
        Trova una lista di sensori secondo i filtri inseriti.
        :param filter: SensorFilter
        :return: Una lista di sensori
        """
        sensorquery = self.collection.find(filter.getConditions())
        sensorslist = [Sensor.to_model(user) for user in sensorquery]
        return sensorslist

    def setvalue(self,sensorid,value):
        """
        Questo metodo aggiunge un valore rilevato ad un sensore.
        :param sensorid: Id del sensore a cui aggiungere una rilevazione
        :return: True
        """
        valuetoadd = Value.from_model(value)
        insertionResult = self.collection.update_one({"_id": ObjectId(sensorid)}, {"$push": {"values": valuetoadd}})
        if not insertionResult.acknowledged:
            raise ValueAddError
        print("Insertion completed", insertionResult.upserted_id)
        return insertionResult.upserted_id
