class TimeFilter:
    def __init__(self,timefrom=None,timeto=None):
        self.timefrom = timefrom
        self.timeto = timeto


    def getConditions(self):
        filterDict = {}
        if self.timefrom is not None:
            filterDict["$gt"] = self.timefrom.isoformat()
        if self.timeto is not None:
            filterDict["$lt"] = self.timeto.isoformat()

        return filterDict
