from marshmallow import Schema,fields

class LoginRequest(Schema):
    username = fields.String(required=True,error_messages={"required" : {"message" : "Username can't be unset"}})
    password = fields.String(required=True,error_messages={"required" : {"message" : "Password can't be unset"}})