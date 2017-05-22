from common.settings import persistenceSettings,authSettings
import flask_bcrypt
from common.services.userservice import UserService
from common.filters.users import UserFilter
from common.filters.orfilter import OrFilter
from common.models.user import User
from common.exceptions.auth import RegisterSameUserError
from flask_jwt_extended import revoke_token

class AuthManager:
    def __init__(self,database):
        self.users = database

    def login(self,username,password):
        """
        Questo metodo effettua il login dell'utente controllando le sue credenziali.
        :param username: Username utente
        :param password: Password utente
        :return: id utente loggato / False
        """
        service = UserService(self.users)
        loginfilter = UserFilter(username=username)
        user = service.find(loginfilter)[0]
        #Check password
        if flask_bcrypt.check_password_hash(pw_hash=user.password,password=password):
            #Login effettuato
            return user.id
        return False


    def logout(self,token):
        """
        Metodo per il logout di un utente, inserisce nella blacklist,ovvero la lista di token non più usabili
        quello passato in input.
        :param token: User jwt token
        :return: True/False
        """
        try:
            jti = token['jti']
            revoke_token(jti)
        except KeyError:
            return False
        return True


    def register(self,username,password,email,role):
        """
        Metodo per registrare un nuovo utente.
        :param username: Username utente
        :param password: Password utente
        :param email: email utente
        :return: id dell'utente registrato / Eccezioni
        """

        #Step 1, controllare che non ci siano altri utenti con lo stesso username o email
        usernamefilter = UserFilter(username=username)
        emailfilter = UserFilter(email=email)
        #Filtro or per controllare in or le due condizioni dei filtri
        orfilter = OrFilter(usernamefilter,emailfilter)
        service = UserService(self.users)
        result = service.find(orfilter)
        if result:
            raise RegisterSameUserError

        #Creazione utente

        newuser = User(username=username,email=email,password=flask_bcrypt.generate_password_hash(password=password),role=role)
        newuserid = service.add(newuser)
        return newuserid


    def is_admin(self,userid):
        """
        Metodo per controllare se un utente abbia o meno i privilegi amministrativi
        :param userid: Id dell'utente
        :return: True/False
        """
        service = UserService(self.users)
        adminfilter = UserFilter(role=1,id=userid)
        if service.find(adminfilter):
            return True
        return False

