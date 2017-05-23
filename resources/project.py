from common.exceptions.project import ProjectNotFoundError,ProjectAddError
from common.services.projects import ProjectService
from common.filters.projects import ProjectFilter
from bson.objectid import ObjectId
from flask_restful import Resource
from common.utils.decorators import is_admindecorator
from common.models.project import ProjectModelView,Project
from flask import request
from flask_jwt_extended import get_jwt_identity,jwt_required
from common.exceptions.project import ProjectAddError,ProjectNotFoundError

import datetime

class GetandAddProjectsForUser(Resource):

    decorators = [jwt_required]

    def __init__(self, **kwargs):
        self.database = kwargs["database"]


    def get(self):
        user_id = get_jwt_identity()
        if not ObjectId.is_valid(user_id):
            return {"message" : "Invalid user id"},500
        filter = ProjectFilter(id=user_id)
        rawProjects = ProjectService(self.database).find(filter=filter)
        if not rawProjects:
            return {"projects" : []},200
        projectsList = ProjectModelView().dump(rawProjects,many=True)
        return {"projects" : projectsList[0]},200

    def post(self):
        user_id = get_jwt_identity()
        validate = ProjectModelView().validate(request.json)
        if validate:
            return validate, 500
        if ObjectId.is_valid(user_id):
            return {"message": "Invalid user id"}, 500
        args = request.json
        service = ProjectService(self.database)
        newproject = Project(name=args["name"],description=args["description"],createdAt=datetime.datetime.now())
        try:
            result = service.add(project=newproject,userid=user_id)
        except ProjectAddError as e:
            return {"message" : e},500
        return {"message" : "Project added for user {0}".format(user_id)}





class GetProjectsAdmin(Resource):

    decorators = [jwt_required]
    method_decorators = [is_admindecorator]

    def __init__(self, **kwargs):
        self.database = kwargs["database"]

    def get(self,user_id):
        if not ObjectId.is_valid(user_id):
            return {"message" : "Invalid user id"},500
        filter = ProjectFilter(id=user_id)
        rawProjects = ProjectService(self.database).find(filter=filter)
        if not rawProjects:
            return {"projects": []}, 200
        projectsList = ProjectModelView().dump(obj=rawProjects, many=True)
        return {"projects": projectsList[0]}, 200


