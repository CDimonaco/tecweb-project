from common.exceptions.project import ProjectNotFoundError,ProjectAddError
from common.services.projects import ProjectService
from common.filters.projects import ProjectFilter
from bson.objectid import ObjectId
from flask_restful import Resource
from common.models.project import ProjectModelView
from flask import request
from flask_jwt_extended import get_jwt_identity,jwt_required


class GetProjectsForUser(Resource):

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
            return {"projects" : []}
        projectsList = ProjectModelView.dump(rawProjects,many=True)
        return {"projects" : projectsList},200


