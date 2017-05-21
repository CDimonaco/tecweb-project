from common.settings import persistenceSettings
from common.exceptions.users import *
from common.models.user import User
from bson.objectid import ObjectId

class UserService:
    def __init__(self,database):
        self.collection = database[persistenceSettings["usersCollection"]]


    def getAll(self):
        #Questo metodo ritorna tutti gli utenti nel database, è utile solo per ragioni di testing
        #Non ritorneremo una lista di oggetti User ma semplicemente i documenti contenuti nella collection degli users
        #Questo infatti è più che sufficiente per il mero testing
        userCursor = self.collection.find(projection={"projects" : False})
        usersList = [user for user in userCursor]
        testUser = {"count" : userCursor.count(),"users" : usersList}
        print(testUser)


    def addOne(self,user):
        #Questo metodo aggiunge un utente al database, prendendo un oggetto user,lo trasforma in un dizionario
        #e lo aggiunge alla collection, ritorna l'id dell'utente aggiunto.
        usertoAdd = User.from_model(user)
        insertionResult = self.collection.insert_one(usertoAdd)
        if not insertionResult.acknowledged:
            raise UserAddError
        print("Insertion completed",insertionResult.inserted_id)
        return insertionResult.inserted_id

    def deleteOne(self,id):
        #Questo metodo elimina un utente
        deleteResult = self.collection.delete_one({"_id" : ObjectId(id)})
        if deleteResult.deleted_count < 1:
            #TODO:ADD LOG TO FLASK
            raise UserNotFoundError
        return True

    def findOne(self,filter):
       #Questo metodo ritorna un solo utente dal database secondo i filtri inseriti
       userQuery = self.collection.find_one(filter.getConditions())
       if not userQuery:
           #TODO:ADD LOG TO FLASK
           raise UserNotFoundError
       userFound = User.to_model(userQuery)
       return userFound
