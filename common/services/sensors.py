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
        return str(insertionResult.inserted_id)

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

    def find(self,filter,offset=0):
        """
        Trova una lista di sensori secondo i filtri inseriti.
        :param filter: SensorFilter
        :param offset: Offset per la paginazione
        :return: Una lista di sensori, more che indica che ci sono ancora elementi da paginare
        """
        sensorquery = self.collection.find(filter.getConditions(),skip=offset,limit=100)
        totalsensors = sensorquery.count()
        sensorslist = [Sensor.to_model(sensor) for sensor in sensorquery]
        print(totalsensors)
        more = offset + 100 < totalsensors
        return sensorslist,more

