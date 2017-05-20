from flask import Flask
import logging
from pymongo import MongoClient
from common.models.user import User
from common.models.sensor import Sensor
app = Flask(__name__)

#Create mongodb client and connect to the database "tecweb"
mongoClient = MongoClient()
mongoDatabase = mongoClient["tecweb"]
#Log setup
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

@app.route('/')
def hello_world():
    app.logger.debug("HERE")
    app.logger.info("INFO")
    return 'Hello World!'


if __name__ == '__main__':
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(consoleHandler)
    app.run()
