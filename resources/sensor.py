from common.exceptions.sensors import SensorNotFoundError,SensorAddError
from common.models.sensor import Sensor,SensorViewModel
from common.filters.sensors import SensorFilter
from common.services.sensors import SensorService
from common.services.values import ValueService
from common.exceptions.values import ValueNotFoundError,ValueAddError
from common.models.value import Value,ValueModelView
from common.filters.values import ValueFilter
from resources.schemas.sensor import AddSensorRequest,AddValueRequest
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask import request
from flask_restful import Resource
from bson.objectid import ObjectId
import uuid
import datetime

class AddandGetSensors(Resource):
    decorators = [jwt_required]

    def __init__(self, **kwargs):
        self.authManager = kwargs["auth_manager"]
        self.database = kwargs["database"]

    def get(self,project_id):
        user_id = get_jwt_identity()
        if not ObjectId.is_valid(user_id):
            return {"message": "Invalid user id"}, 500
        if not ObjectId.is_valid(project_id):
            return {"message": "Invalid project id id"}, 500
        if request.args.get("offset") is None:
            return {"message" : "Offset can't be unset"},500
        offset = int(request.args.get("offset"))
        is_admin = self.authManager.is_admin(user_id=user_id)
        if is_admin:
            filter = SensorFilter(project=[project_id])
            filtersRaw,hasmore = SensorService(self.database).find(filter,offset=offset)
            filtersList = SensorViewModel().dump(filtersRaw,many=True)
            return {"sensors" : filtersList[0],"hasMore" : hasmore},200
        #Controllo se l'utente è il propietario del progetto
        if not self.authManager.project_owner(userid=user_id,projectid=project_id):
            return {"message" : "You are not the owner of project"},401
        filter = SensorFilter(project=[project_id])
        filtersRaw, hasmore = SensorService(self.database).find(filter, offset=offset)
        filtersList = SensorViewModel().dump(filtersRaw, many=True)
        return {"sensors": filtersList[0], "hasMore": hasmore}, 200

    def post(self,project_id):
        user_id = get_jwt_identity()
        if not ObjectId.is_valid(user_id):
            return {"message": "Invalid user id"}, 500
        if not ObjectId.is_valid(project_id):
            return {"message": "Invalid project id id"}, 500
        if not self.authManager.project_owner(userid=user_id,projectid=project_id):
            return {"message" : "You are not the owner of project"},401
        validate = AddSensorRequest().validate(request.json)
        if validate:
            return validate,500
        args = request.json
        apikey = str(uuid.uuid4())
        newsensor = Sensor(name=args["name"],apikey=apikey,project=project_id)
        try:
            inserted_id = SensorService(self.database).add(newsensor)
        except SensorAddError as e:
            return {"message" : str(e)},500
        return {"newsensor" : inserted_id,"apikey" : apikey},200



class DeleteSensor(Resource):

    decorators = [jwt_required]

    def __init__(self, **kwargs):
        self.authManager = kwargs["auth_manager"]
        self.database = kwargs["database"]

    def delete(self,project_id,sensor_id):
        user_id = get_jwt_identity()
        if not ObjectId.is_valid(user_id):
            return {"message": "Invalid user id"}, 500
        if not ObjectId.is_valid(sensor_id):
            return {"message": "Invalid sensor id"}, 500
        if not ObjectId.is_valid(project_id):
            return {"message": "Invalid project id id"}, 500
        if not self.authManager.project_owner(userid=user_id,projectid=project_id):
            return {"message" : "You are not the owner of project"},401
        service = SensorService(self.database)
        filter = SensorFilter(project=[project_id],id=[sensor_id])
        try:
            service.delete(filter=filter)
        except SensorNotFoundError as e:
            return {"message" : str(e)},500
        return 400


class AddValueGetValue(Resource):

    def __init__(self, **kwargs):
        self.database = kwargs["database"]
        self.authManager = kwargs["auth_manager"]

    def post(self,sensor):
        api_key = sensor
    #L'api key è un UUID4, dobbiamo validare ciò che ci viene in entrata.
        try:
            uuid.UUID(api_key)
        except ValueError:
            return {"message" : "Invalid Api key"},500
        validate = AddValueRequest().validate(request.json)
        if validate:
            return validate,500
        args = request.json
        if "additional" not in args:
            additional = ""
        else:
            additional = args["additional"]
        #Trovo il sensore per quell'api key
        filter = SensorFilter(apikey=api_key)
        result,_ = SensorService(self.database).find(filter=filter)
        if not result:
            return {"message" : "Impossible to assign the value"},404
        sensor_id = result[0].id
        new_value = Value(value=args["value"],timestamp=datetime.datetime.now(),sensorid=sensor_id,additional=additional)
        try:
            inserted_id = ValueService(self.database).add(new_value)
        except ValueAddError:
            return {"message" : "impossibile to add value"},500
        return {"message" : "Value added for sensor {}".format(str(sensor_id))}

    @jwt_required
    def get(self,sensor):
        #Recupero il progetto associato al sensore di cui voglio i valori
        user_id = get_jwt_identity()
        if not ObjectId.is_valid(user_id):
            return {"message": "Invalid user id"}, 500
        if not ObjectId.is_valid(sensor):
            return {"message": "Invalid sensor id"}, 500
        if request.args.get("offset") is None:
            return {"message" : "Offset can't be unset"},500
        offset = int(request.args.get("offset"))
        filter = SensorFilter(id=[sensor])
        project,_ = SensorService(self.database).find(filter=filter)
        if not project:
            return {"message" : "Invalid sensor id,no project associated to the sensor"},404
        project_id = project[0].project
        #Se è un admin
        if self.authManager.is_admin(user_id=user_id):
            valuesfilter = ValueFilter(sensorid=sensor)
            valuesRaw, more = ValueService(self.database).find(filter=valuesfilter,offset=offset)
            values = ValueModelView().dump(valuesRaw, many=True)
            return {"values": values[0], "hasMore": more}, 200
        if not self.authManager.project_owner(user_id,project_id):
            return {"message" : "You are not the owner of project"},401
        #Se sono il titolare del progetto, e quindi del sensore, posso passare a ricevere i valori.
        valuesfilter = ValueFilter(sensorid=sensor)
        valuesRaw,more = ValueService(self.database).find(filter=valuesfilter,offset=offset)
        values = ValueModelView().dump(valuesRaw,many=True)
        return {"values" : values[0],"hasMore" : more},200












