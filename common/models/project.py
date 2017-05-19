class Project:
    def __init__(self,name,description,createdAt):
        self.name = name
        self.description = description
        self.createdAt = createdAt


    @staticmethod
    def to_model(mongoproject):
        return Project(str(mongoproject["_id"],mongoproject["name"],mongoproject["description"],mongoproject["createdAt"]))
    #TODO:Add date object for createdAt, convert from ISOString to datetime.date, also in from_model static method

    @staticmethod
    def from_model(appproject):
        mongoDict = {
            "name" : appproject.name,
            "description" : appproject.description,
            "createdAt" : appproject.createdAt
        }
        return mongoDict
