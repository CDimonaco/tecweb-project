from common.exceptions.sensors import SensorNotFoundError,SensorAddError
from common.models.sensor import Sensor,SensorViewModel
from common.filters.sensors import SensorFilter
from common.services.sensors import SensorService
from resources.schemas.sensor import AddSensorRequest
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask import request
from flask_restful import Resource
from bson.objectid import ObjectId

class AddandGetSensors(Resource):
    decorators = [jwt_required]

    def __init__(self, **kwargs):
        self.authManager = kwargs["auth_manager"]
        self.database = kwargs["database"]

    def get(self,project_id):
        user_id = get_jwt_identity()
        if not ObjectId.is_valid(user_id):
            return {"message": "Invalid user id"}, 500
        if request.args.get("offset") is None:
            return {"message" : "Offset can't be unset"},500
        offset = int(request.args.get("offset"))
        is_admin = self.authManager.is_admin(user_id=user_id)
        if is_admin:
            filter = SensorFilter(project=project_id)
            filtersRaw,hasmore = SensorService(self.database).find(filter,offset=offset)
            filtersList = SensorViewModel().dump(filtersRaw,many=True)
            return {"sensors" : filtersList[0],"hasMore" : hasmore},200



