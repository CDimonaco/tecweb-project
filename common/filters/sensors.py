from bson.objectid import ObjectId


class SensorFilter:
    def __init__(self,id=None,name=None,project=None,apikey=None):
        self.id = id
        self.name = name
        self.project = project
        self.apikey = apikey



    def getConditions(self):
        filterDict = {}

        if self.id is not None:
            filterDict["_id"] = {"$in" : [ObjectId(id) for id in self.id]}
        if self.name is not None:
            filterDict["name"] = self.name
        if self.project is not None:
            filterDict["project"] = {"$in" : [ObjectId(id) for id in self.project]}
        if self.apikey is not None:
            filterDict["apikey"] = self.apikey

        return filterDict

