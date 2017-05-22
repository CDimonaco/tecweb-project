from flask_restful import reqparse,Resource,request
from common.utils.decorators import is_admindecorator
from flask_jwt_extended import jwt_required
from common.exceptions.auth import RegisterSameUserError
from common.exceptions.users import UserNotFoundError
from common.services.userservice import UserService
from common.filters.users import UserFilter
from resources.schemas.user import AddUserRequest


class AddandRemove(Resource):
    #decorators = [jwt_required]
    #method_decorators = [is_admindecorator]

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

    """def delete(self):
        args = _delete_user_parser.parse_args()
        service = UserService(self.database)
        filter = UserFilter(id=args.userid)
        try:
            service.delete(filter)
        except UserNotFoundError:
            return {"message": "user not found"}, 404

        return 400"""



class Test(Resource):

    def post(self):
        print(request.json["username"])
        return 200



class GetUsers(Resource):

    decorators = [jwt_required]
    method_decorators = [is_admindecorator]

    def __init__(self, **kwargs):
        self.database = kwargs["database"]

