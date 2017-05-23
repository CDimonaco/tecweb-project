from marshmallow import Schema,fields

class AddSensorRequest(Schema):
    name = fields.String(required=True,error_messages={"required" : "Name can't be unset"})
    apikey = fields.String(required=True,error_messages={"required" : "Apikey can't be unset"})
    project = fields.String(required=True,error_messages={"required" : "Project can't be unset"})
