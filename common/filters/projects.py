from bson.objectid import ObjectId

"""
Filtro per i progetti
N.B. CreatedAt deve time filter
"""
class ProjectFilter:
    def __init__(self,id=None,description=None,createdAt=None):
        self.id = id
        self.description=description
        self.createdAt = createdAt


    def getConditions(self):
        filterDict =  {}

        if self.id is not None:
            filterDict["_id"] = ObjectId(self.id)
        if self.description is not None:
            filterDict["description"] = self.description
        if self.createdAt is not None:
            filterDict["createdAt"] = self.createdAt.getConditions()

        return filterDict