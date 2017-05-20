class Value:
    def __init__(self,value,additional,id=""):
        self.id = id
        self.value = value
        self.additional = additional

    def __str__(self):
        return "<Value>: "+self.id+" "+self.value+" "+self.additional

    @staticmethod
    def to_model(mongovalue):
        return Value(id=str(mongovalue["_id"]),value=mongovalue["value"],additional=mongovalue["additional"])

    @staticmethod
    def from_model(appvalue):
        mongoDict = {
            "value" : appvalue.value,
            "additional" : appvalue.additional
        }
        return mongoDict
