class Sensor:
    def __init__(self,id,name,apikey):
        self.id = id
        self.name = name
        self.apikey = apikey

    def __str__(self):
        return "<Sensor>:"+self.name+self.id+self.apikey

    @staticmethod
    def to_model(mongosensor):
        return Sensor(str(mongosensor["_id"]),mongosensor["name"],mongosensor["apikey"])

    @staticmethod
    def from_model(appsensor):
        sensorDict = {
            "name" : appsensor.name,
            "apikey" : appsensor.apikey
        }
        return sensorDict