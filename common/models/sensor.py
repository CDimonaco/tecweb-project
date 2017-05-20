class Sensor:
    def __init__(self,name,apikey,project,id=""):
        self.id = id
        self.name = name
        self.project = project
        self.apikey = apikey

    def __str__(self):
        return "<Sensor>: "+self.name+" "+self.id+" "+self.apikey+" "+self.project

    @staticmethod
    def to_model(mongosensor):
        return Sensor(id=str(mongosensor["_id"]),name=mongosensor["name"],apikey=mongosensor["apikey"],project=str(mongosensor["project"]))

    @staticmethod
    def from_model(appsensor):
        sensorDict = {
            "name" : appsensor.name,
            "apikey" : appsensor.apikey,
            "project" : appsensor.project,
            "values" : []
        }
        return sensorDict