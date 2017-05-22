from marshmallow import Schema,fields

class AddUserRequest(Schema):
    username = fields.String(required=True,error_messages={"required" : "Username can't be unset"})
    password = fields.String(required=True,error_messages={"required" : "Password can't be unset"})
    email = fields.Email(required=True,error_messages={"required" : {"message":"Email can't be unset"}})
    role = fields.Integer(required=True,error_messages={"required" : "Role can't be unset"})

