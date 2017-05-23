from marshmallow import Schema,fields

class User:
    def __init__(self,username,password,email,role,id=""):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        self.email = email


    def getRole(self):
        return self.role

    def __eq__(self, other):
        """Override del metodo __eq__ necessario per il testing."""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        """ Definisce quando due oggetti non sono uguali. Necessario per il testing"""
        return not self.__eq__(other)


    def __str__(self):
        return "<User>: "+self.id+" "+self.username+" "+self.password+" "+str(self.role)+" "+self.email

    @staticmethod
    def to_model(mongouser):
        return User(id=str(mongouser["_id"]),username=mongouser["username"],password=mongouser["password"],email=mongouser["email"],role=mongouser["role"])

    @staticmethod
    def from_model(appuser):
        mongoDict = {
            "username" : appuser.username,
            "password" : appuser.password,
            "role" : appuser.role,
            "email" : appuser.email,
        }
        return mongoDict


class UserViewModel(Schema):
    id = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    role = fields.Integer(required=True)
    email = fields.Email(required=True)

