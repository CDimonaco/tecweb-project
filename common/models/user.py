class User:
    def __init__(self,id,name,surname,role):
        self.id = id
        self.name = name
        self.surname = surname
        self.role = role

    def __str__(self):
        return "<User>:"+self.id+self.name+self.surname+self.role

    @staticmethod
    def to_model(mongouser):
        return User(str(mongouser["_id"]),mongouser["username"],"Lol","Lol")

    @staticmethod
    def from_model(appuser):
        mongoDict = {
            "username" : appuser.name,
        }
        return mongoDict