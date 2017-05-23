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

        if self.sensorid is not None:
            filterDict["sensorid"] = ObjectId(self.sensorid)
        if self.id is not None:
            filterDict["_id"] = ObjectId(self.id)
        if self.value is not None:
            filterDict["value"] = self.value
        if self.timestamp is not None:
            filterDict["timestamp"] = self.timestamp.getConditions()
        if self.additional is not None:
            filterDict["additional"] = self.additional

        return filterDict