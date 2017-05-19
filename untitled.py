from flask import Flask
from pymongo import MongoClient
from common.models.user import User
from common.models.sensor import Sensor
app = Flask(__name__)

#Create mongodb client and connect to the database "tecweb"
mongoClient = MongoClient()
mongoDatabase = mongoClient["tecweb"]

@app.route('/')
def hello_world():
    collection = mongoDatabase["user"]
    sensor = Sensor(id="",name="Pompa",apikey="lolll")
    collection.update_one(filter={"username" : "carmine"},update={
        "$push" : {
            "sensors" :
                    Sensor.from_model(sensor)
        }
    })


    return 'Hello World!'


if __name__ == '__main__':
    app.run()
