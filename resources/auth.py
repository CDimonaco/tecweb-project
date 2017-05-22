from flask_restful import fields, marshal_with, reqparse, Resource,HTTPException
from flask_jwt_extended import create_access_token,jwt_required,get_raw_jwt
from common.exceptions.auth import RegisterSameUserError

#Parser per il login,uso bundle_errors=True per mostrare correttamente i due messaggi di errore
_login_parser = reqparse.RequestParser(bundle_errors=True)
_login_parser.add_argument("username",type=str,help="Username can't be unset",required=True,location="json")
_login_parser.add_argument("password",type=str,help="Password can't be unset",required=True,location="json")

class AuthLogin(Resource):
    def __init__(self,**kwargs):
        self.authManager = kwargs["auth_manager"]

    def post(self):
        args = _login_parser.parse_args()
        username = args["username"]
        password = args["password"]
        print(username,password)
        if self.authManager.login(username,password):
            token = create_access_token(identity=username)
            return {"accessToken" : token}
        return {"message" : "INVALID CREDENTIALS"},401



class AuthLogout(Resource):
    decorators = [jwt_required]
    def __init__(self,**kwargs):
        self.authManager = kwargs["auth_manager"]

    def post(self):
        try:
            self.authManager.logout(get_raw_jwt())
        except KeyError:
           return {"message" : "Invalid token"},500
        return {"message" : "Successfully logout"},200






