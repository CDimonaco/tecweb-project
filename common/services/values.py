from common.settings import persistenceSettings
from common.models.value import Value
from common.exceptions.values import ValueNotFoundError,ValueAddError
class ValueService:
    def __init__(self,database):
        self.collection = database[persistenceSettings["valueCollection"]]


    def getall(self):
        """Questo metodo ritorna tutti i valori rilevati nel database, è utile solo per ragioni di testing
          Non ritorneremo una lista di oggetti User ma semplicemente i documenti contenuti nella collection dei values
          Questo infatti è più che sufficiente per il mero testing"""
        valueCursor = self.collection.find()
        valueslist = [user for user in valueCursor]
        testvalues = {"count" : valueCursor.count(),"users" : valueslist}
        print(testvalues)


    def add(self,value):
        """Questo metodo aggiunge un valore al database, prendendo un oggetto value,lo trasforma in un dizionario
        e lo aggiunge alla collection, ritorna l'id del value aggiunto."""
        valuetoadd = Value.from_model(value)
        insertionResult = self.collection.insert_one(valuetoadd)
        if not insertionResult.acknowledged:
            raise ValueAddError
        print("Insertion completed",insertionResult.inserted_id)
        return insertionResult.inserted_id

    def delete(self,filter):
        """Questo metodo elimina rilevazioni"""
        deleteResult = self.collection.delete_many(filter.getConditions())
        if deleteResult.deleted_count < 1:
            #TODO:ADD LOG TO FLASK
            raise ValueNotFoundError
        return True

    def find(self,filter,offset=0):
       """Questo metodo ritorna utenti dal database secondo i filtri inseriti"""
       valuesQuery = self.collection.find(filter=filter.getConditions(),limit=100,skip=offset)
       totalvalues = valuesQuery.count()
       usersList = [Value.to_model(value) for value in valuesQuery]
       more = offset + 10 < totalvalues
       return usersList,more
