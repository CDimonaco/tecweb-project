from common.settings import persistenceSettings
from common.models.user import User
class UserService:
    def __init__(self,database):
        self.collection = database[persistenceSettings["usersCollection"]]


    def get_allUsers(self):
        #Questo metodo ritorna tutti gli utenti nel database, è utile solo per ragioni di testing
        #Non ritorneremo una lista di oggetti User ma semplicemente i documenti contenuti nella collection degli users
        #Questo infatti è più che sufficiente per il mero testing
        userCursor = self.collection.find(projection={"projects" : False})
        usersList = [user for user in userCursor]
        testUser = {"count" : userCursor.count(),"users" : usersList}
        print(testUser)

    def add_one(self,user):
        usertoAdd = User.from_model(user)
        insertionResult = self.collection.insert_one(usertoAdd)
        print("Insertion completed",insertionResult.inserted_id)
        return insertionResult.inserted_id