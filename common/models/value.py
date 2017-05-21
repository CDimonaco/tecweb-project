class Value:
    def __init__(self,value,timestamp,additional,id=""):
        self.id = id
        self.value = value
        self.timestamp = timestamp
        self.additional = additional

    def __str__(self):
        return "<Value>: "+self.id+" "+self.value+" "+self.additional + " " + self.timestamp

    @staticmethod
    def to_model(mongovalue):
        return Value(id=str(mongovalue["_id"]),value=mongovalue["value"],additional=mongovalue["additional"],timestamp=mongovalue["timestamp"])

    @staticmethod
    def from_model(appvalue):
        mongoDict = {
            "value" : appvalue.value,
            "additional" : appvalue.additional,
            "timestamp" : appvalue.timestamp
        }
        return mongoDict
