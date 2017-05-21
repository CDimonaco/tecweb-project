from bson.objectid import ObjectId

"""
Filtro per i progetti
N.B. CreatedAt deve time filter
"""
class ProjectFilter:
    def __init__(self,id=None,projectid=None,description=None,createdAt=None):
        self.id = id
        self.description=description
        self.createdAt = createdAt
        self.projectid= projectid


    def getConditions(self):
        filterDict =  {}
        filterDict["projects"] = {"$exists": True}
        if self.id is not None:
            filterDict["_id"] = ObjectId(self.id)
        if self.projectid is not None:
            filterDict["projects.id"] = ObjectId(self.projectid)
        if self.description is not None:
            filterDict["projects.description"] = self.description
        if self.createdAt is not None:
            filterDict["projects.createdAt"] = self.createdAt.getConditions()

        return filterDict