from marshmallow import Schema,fields

class AddProjectRequest(Schema):
    name = fields.String(required=True,error_messages={"required" : "Name can't be unset"})
    description = fields.String(required=True,error_messages={"required" : "Description can't be unset"})
