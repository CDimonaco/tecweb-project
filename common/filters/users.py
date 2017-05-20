"""
Classe UserFilter, settiamo le condizioni che vogliamo filtrare passando gli opportuni parametri al costruttore,
l'utilizzo dei filtri ci permette di essere più flessibile sulla query al db, inoltre ci permette con un solo metodo 
nel service di poter filtrare i risultati in base alle nostre esigenze.

Il filter con il metodo getConditions(), ritorna un dizionario con le condizioni da noi scelte compatibile con la 
query diretta a mongodb.
"""
from bson.objectid import ObjectId

class UserFilter:
    def __init__(self,username=None,password=None,id=None,role=None,email=None):
        self.username=username
        self.password=password
        self.id = id
        self.role = role
        self.email = email


    def getCondition(self):
        filterDict = {}
        if self.username is not None:
            filterDict["username"] = self.username
        if self.password is not None:
            filterDict["password"] = self.password
        if self.id is not None:
            filterDict["_id"] = ObjectId(self.id)
        if self.role is not None:
            filterDict["role"] = self.role
        if self.email is not None:
            filterDict["email"] = self.email

        return filterDict


