class OrFilter:

    def __init__(self,*filters):
        self.filters = filters

    def getConditions(self):
        filterDict = {}
        filterDict["$or"] = []

        for filter in self.filters:
            filterDict["$or"].append(filter.getConditions())

        return filterDict