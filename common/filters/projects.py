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
        if self.id is not None:
            filterDict["_id"] = ObjectId(self.id)
        if self.projectid is not None:
            filterDict["project._id"] = ObjectId(self.projectid)
        if self.description is not None:
            filterDict["project.description"] = self.description
        if self.createdAt is not None:
            filterDict["project.createdAt"] = self.createdAt.getConditions()

        return filterDict