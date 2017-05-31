from flask_restful import reqparse,Resource,request
from common.utils.decorators import is_admindecorator
from flask_jwt_extended import jwt_required
from common.exceptions.auth import RegisterSameUserError
from common.exceptions.users import UserNotFoundError
from common.services.userservice import UserService
from common.filters.users import UserFilter
from resources.schemas.user import AddUserRequest
from bson.objectid import ObjectId
from common.models.user import UserViewModel

class AddandGet(Resource):
    decorators = [jwt_required]
    method_decorators = [is_admindecorator]

    def __init__(self, **kwargs):
        self.authManager = kwargs["auth_manager"]
        self.database = kwargs["database"]

    def post(self):
        validate = AddUserRequest().validate(request.json)
        if validate:
            return validate,500
        args = request.json
        try:
            newid = self.authManager.register(username=args["username"],password=args["password"],role=args["role"],email=args["email"])
        except RegisterSameUserError:
            return {"message" : "Impossibile creare l'utente, controlla che non ne esista già uno con le stesse credenziali"},500

        return {"newuser" : str(newid)},200

    def get(self):
        if request.args.get("offset") is None:
            return {"message" : "Offset can't be unset"},500
        offset = int(request.args.get("offset"))
        userfilter = UserFilter()
        usersRaw,more = UserService(self.database).find(filter=userfilter,offset=offset)
        userlist = UserViewModel().dump(usersRaw,many=True)
        return {"users" : userlist[0], "hasMore" : more}



class DeleteUser(Resource):

    decorators = [jwt_required]
    method_decorators = [is_admindecorator]

    def __init__(self, **kwargs):
        self.database = kwargs["database"]

    def delete(self,user_id):
            print(user_id)
            if not ObjectId.is_valid(user_id):
                return {"message" : "Invalid user id"},500
            service = UserService(self.database)
            filter = UserFilter(id=user_id)
            try:
                service.delete(filter)
            except UserNotFoundError:
                return {"message": "user not found"}, 404
            return 400