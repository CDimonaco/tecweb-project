from common.settings import persistenceSettings
from common.exceptions.users import *
from common.models.user import User
from common.services.sensors import SensorService
from common.services.projects import ProjectService
from common.filters.projects import ProjectFilter
from common.filters.sensors import SensorFilter

class UserService:
    def __init__(self,database):
        self.collection = database[persistenceSettings["usersCollection"]]


    def getall(self):
        """Questo metodo ritorna tutti gli utenti nel database, è utile solo per ragioni di testing
          Non ritorneremo una lista di oggetti User ma semplicemente i documenti contenuti nella collection degli users
          Questo infatti è più che sufficiente per il mero testing"""
        userCursor = self.collection.find(projection={"projects" : False})
        usersList = [user for user in userCursor]
        testUser = {"count" : userCursor.count(),"users" : usersList}
        print(testUser)


    def add(self,user):
        """Questo metodo aggiunge un utente al database, prendendo un oggetto user,lo trasforma in un dizionario
        e lo aggiunge alla collection, ritorna l'id dell'utente aggiunto."""
        usertoAdd = User.from_model(user)
        insertionResult = self.collection.insert_one(usertoAdd)
        if not insertionResult.acknowledged:
            raise UserAddError
        print("Insertion completed",insertionResult.inserted_id)
        return insertionResult.inserted_id

    def delete(self,filter):
        """Questo metodo elimina utenti,eliminandone anche i sensori e i valori associati a quei sensori"""
        conditions = filter.getConditions()
        #Mi è più comodo ai fini della procedura inserire le condizioni dei filtri in una variabile.
        # Recupero tutti i progetti dell'utente per cancellarne i sensori
        ps = ProjectService(self.collection.database)
        pf = ProjectFilter(id=str(conditions["_id"]))
        projectList = ps.find(pf)
        idprojects = [project.id for project in projectList]
        print(idprojects)
        sensorService = SensorService(self.collection.database)
        sensorfilter = SensorFilter(project=idprojects)
        sensordeleteResult = sensorService.delete(sensorfilter)
        deleteResult = self.collection.delete_many(filter.getConditions())
        if deleteResult.deleted_count < 1:
            #TODO:ADD LOG TO FLASK
            raise UserNotFoundError
        return True

    def find(self,filter,offset=0):
       """Questo metodo ritorna utenti dal database secondo i filtri inseriti"""
       userQuery = self.collection.find(filter=filter.getConditions(),limit=100,skip=offset)
       totalusers = userQuery.count()
       usersList = [User.to_model(user) for user in userQuery]
       print(totalusers)
       more = offset + 100 < totalusers
       return usersList, more
