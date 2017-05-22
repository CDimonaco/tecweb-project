from flask_restful import reqparse,Resource,request
from common.utils.decorators import is_admindecorator
from flask_jwt_extended import jwt_required
from common.exceptions.auth import RegisterSameUserError
from common.exceptions.users import UserNotFoundError
from common.services.userservice import UserService
from common.filters.users import UserFilter
from marshmallow import Schema,fields


_add_user_parser = reqparse.RequestParser(bundle_errors=True)
_add_user_parser.add_argument("username",type=str,help="Username can't be unset",required=True,location="json")
_add_user_parser.add_argument("password",type=str,help="Password can't be unset",required=True,location="json")
_add_user_parser.add_argument("email",type=str,help="Email can't be unset",required=True,location="json")
_add_user_parser.add_argument("role",type=int,help="Role can't be unset",required=True,location="json")

_delete_user_parser = reqparse.RequestParser()
_delete_user_parser.add_argument("userid",type=str,help="Userid can't be unset",required=True,location="json")

class AddUserRequest(Schema):
    username = fields.String(required=True,error_messages={"required" : "Username can't be unset"})
    password = fields.String(required=True,error_messages={"required" : "Password can't be unset"})
    email = fields.Email(required=True,error_messages={"required" : {"message":"Email can't be unset"}})
    role = fields.Integer(required=True,error_messages={"required" : "Role can't be unset"})

class AddandRemove(Resource):
    decorators = [jwt_required]
    method_decorators = [is_admindecorator]

    def __init__(self, **kwargs):
        self.authManager = kwargs["auth_manager"]
        self.database = kwargs["database"]

    def post(self):

        try:
            newid = self.authManager.register(username=args.username,password=args.password,role=args.role,email=args.email)
        except RegisterSameUserError:
            return {"message" : "Impossibile creare l'utente, controlla che non ne esista già uno con le stesse credenziali"},500

        return {"newuser" : newid},200

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

