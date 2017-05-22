from unittest import TestCase
from pymongo import MongoClient
from common.utils.auth import AuthManager
from common.exceptions.auth import RegisterSameUserError

class TestAuth(TestCase):
    def setUp(self):
        self.database = MongoClient().tecweb
        self.manager = AuthManager(self.database)


    def test_registerValidUser(self):
        newid = self.manager.register(username="ciccio",password="lllll",email="lol@sd.com",role=0)
        print("New user with id",newid)

    def test_registerInvalidUser(self):
        try:
            newid = self.manager.register(username="Ciao", password="Miao", email="lol@asd.com", role=0)
        except RegisterSameUserError:
            print("Impossibile registrare un utente,test superato")
            pass

    def test_login(self):
        loggedid = self.manager.login(username="Ciao",password="Miao")
        print(loggedid)
        self.assertTrue(loggedid)
