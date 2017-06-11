from common.settings import persistenceSettings
from common.exceptions.project import ProjectNotFoundError,ProjectAddError
from common.models.project import Project
from bson.objectid import ObjectId
from common.filters.sensors import SensorFilter
from common.services.sensors import SensorService
from common.exceptions.sensors import SensorNotFoundError

class ProjectService:
    def __init__(self,database):
        self.collection = database[persistenceSettings["usersCollection"]]


    def getall(self):
        """Questo metodo mi ritorna tutti i progetti, usato solo in fase di testing
            Effettuo una proiezione mostrando solo gli embedded documents projects
        """
        projectCursor = self.collection.find({},{"projects":1,"_id":0})
        projectList = [projects for projects in projectCursor]
        testProjects = {"count":projectCursor.count(),"projects" : projectList}
        return testProjects

    def add(self,userid,project):
        """Questo metodo aggiunge un progetto al database, prendendo un oggetto project,lo trasforma in un dizionario
        e lo aggiunge alla collection, dato che è un embedded document si tratterà di aggiornare il documento padre
        in questo caso user, passo al metodo l'id dell'utente a cui verrà aggiunto il progetto
        N.B. Avrei potuto anche usare UserFilter, aggiungere solo la condizione '_id' e fare l'update. per non aumentare
        inutilmente la complessità e sopratutto perchè sarà sempre e solo quel campo ho optato per la soluzione proposta."""
        projectToAdd = Project.from_model(project)
        insertionResult = self.collection.update_one({"_id" : ObjectId(userid)},{"$push":{"projects":projectToAdd}})
        if not insertionResult.acknowledged or insertionResult.modified_count < 0:
            raise ProjectAddError
        print("Insertion completed for user", userid)
        return userid

    def delete(self,projectid,userid):
        """
        Questo metodo cancella un progetto, come si nota è inserito come parametro oltre l'id del progetto
        anche l'id dell'utente propietario del progetto stesso.
        Tale accorgimento è inserito per evitare che un utente possa cancellare progetti di un altro utente.
        Quando si cancella un progetto, verranno cancellati dal sistema anche tutti i sensori ad esso associati.
        :param userid: Id dell'utente proprietario del progetto
        :param projectid: Id del progetto da cancellare
        :return: True
        """
        deleteprojectresult = self.collection.update_one({"_id": ObjectId(userid)}, {"$pull": {"projects": {"id" : ObjectId(projectid)}}})
        if deleteprojectresult.modified_count < 1:
            raise ProjectNotFoundError
        sensordeletefilter = SensorFilter(project=[projectid])
        deletesensorsresult = SensorService(self.collection.database).delete(sensordeletefilter)
        if not deletesensorsresult:
            raise SensorNotFoundError
        return True

    def find(self,filter):
        """
        Questo metodo trova progetti secondo il filtro inserito.
        :param filter: ProjectFilter
        :return: Una lista di progetti
        """
        projectsquery = self.collection.find(projection={"_id": False, "username": False, "password": False, "role": False,"email":False},filter=filter.getConditions())
        elements = [value for value in projectsquery]
        projectlist = []
        for result in elements:
            for projects  in result["projects"]:
                projectlist.append(Project.to_model(projects))
        print(elements)
        print(projectlist)
        return projectlist



