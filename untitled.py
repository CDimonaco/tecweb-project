from flask import Flask
import logging
import datetime
from pymongo import MongoClient
import simplekv.db.mongo
from common.utils.auth import AuthManager
from resources.project import GetandAddProjectsForUser,GetProjectsAdminAndDelete
from resources.sensor import AddandGetSensors,DeleteSensor,AddValueGetValue
from flask_restful import Api,abort
from resources.auth import AuthLogin,AuthLogout
from resources.users import Test,AddandGet,DeleteUser
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix

mongoClient = MongoClient()
mongoDatabase = mongoClient["tecweb"]
authManager = AuthManager(database=mongoDatabase)
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app=app)
app.secret_key = "sosecretlol"
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_STORE'] = simplekv.db.mongo.MongoStore(db=mongoDatabase,collection="tokens")
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = 'all'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=5)
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
jwt = JWTManager(app)
CORS(app)


api.add_resource(Test,"/api/test")

api.add_resource(AddandGet,"/user",resource_class_kwargs={ 'auth_manager': authManager ,"database" : mongoDatabase})
api.add_resource(DeleteUser,"/user/<user_id>",resource_class_kwargs={"database" : mongoDatabase})

api.add_resource(GetandAddProjectsForUser,"/projects",resource_class_kwargs={"database" : mongoDatabase})
api.add_resource(GetProjectsAdminAndDelete,"/projects/<id>",resource_class_kwargs={"database" : mongoDatabase})

api.add_resource(AddandGetSensors,"/sensors/<project_id>",resource_class_kwargs={ 'auth_manager': authManager ,"database" : mongoDatabase})
api.add_resource(DeleteSensor,"/sensors/<project_id>/<sensor_id>",resource_class_kwargs={ 'auth_manager': authManager ,"database" : mongoDatabase})
api.add_resource(AddValueGetValue,"/sensors/value/<sensor>",resource_class_kwargs={"database" : mongoDatabase,'auth_manager': authManager })

api.add_resource(AuthLogin,"/auth/login",resource_class_kwargs={ 'auth_manager': authManager })
api.add_resource(AuthLogout,"/auth/logout",resource_class_kwargs={ 'auth_manager': authManager })


if __name__ == '__main__':
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(consoleHandler)
    app.run(threaded=True)
