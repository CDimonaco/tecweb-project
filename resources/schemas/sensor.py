from marshmallow import Schema,fields

class AddSensorRequest(Schema):
    name = fields.String(required=True,error_messages={"required" : "Name can't be unset"})