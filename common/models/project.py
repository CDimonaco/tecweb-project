class Project:
    def __init__(self,name,description,createdAt,id=""):
        self.id = id
        self.name = name
        self.description = description
        self.createdAt = createdAt


    @staticmethod
    def to_model(mongoproject):
        return Project(id=str(mongoproject["_id"]),name=mongoproject["name"],description=mongoproject["description"],createdAt=mongoproject["createdAt"])
    #TODO:Add date object for createdAt, convert from ISOString to datetime.date, also in from_model static method

    @staticmethod
    def from_model(appproject):
        mongoDict = {
            "name" : appproject.name,
            "description" : appproject.description,
            "createdAt" : appproject.createdAt
        }
        return mongoDict
