class User:
    def __init__(self,username,password,email,role,id=""):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        self.email = email

    def __str__(self):
        return "<User>: "+self.id+" "+self.username+" "+self.password+" "+self.role+" "+self.email

    @staticmethod
    def to_model(mongouser):
        return User(id=str(mongouser["_id"]),username=mongouser["username"],password=mongouser["password"],email=mongouser["email"],role=mongouser["role"])

    @staticmethod
    def from_model(appuser):
        mongoDict = {
            "username" : appuser.name,
            "password" : appuser.password,
            "role" : appuser.role,
            "email" : appuser.email,
            "projects" : [],
        }
        return mongoDict