from marshmallow import Schema,fields

class AddSensorRequest(Schema):
    name = fields.String(required=True,error_messages={"required" : "Name can't be unset"})

class AddValueRequest(Schema):
    value = fields.Float(required=True,error_messages={"required" : "Value can't be unset"})
    additional = fields.String()



