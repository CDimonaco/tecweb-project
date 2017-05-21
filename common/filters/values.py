from bson.objectid import ObjectId

class ValueFilter:
    def __init__(self,sensorid=None,id=None,value=None,timestamp=None,additional=None):
        self.id = id
        self.value = value
        self.timestamp = timestamp
        self.additional = additional
        self.sensorid = sensorid


    def getConditions(self):
        filterDict = {}
        #Filtro necessario.
        filterDict["values"] = {"$exists" : True}
        if self.sensorid is not None:
            filterDict["_id"] = self.sensorid
        if self.id is not None:
            filterDict["values.id"] = ObjectId(self.id)
        if self.value is not None:
            filterDict["values.value"] = self.value
        if self.timestamp is not None:
            filterDict["values.timestamp"] = self.timestamp.getConditions()
        if self.additional is not None:
            filterDict["values.additional"] = self.additional

        return filterDict