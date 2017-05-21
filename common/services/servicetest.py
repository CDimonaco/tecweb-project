from unittest import TestCase
from pymongo import MongoClient
from common.services.userservice import UserService
from common.filters.users import UserFilter
from common.exceptions.users import UserNotFoundError,UserAddError

class TestUserService(TestCase):
    def setUp(self):
        self.database = MongoClient().tecweb
        self.service = UserService(self.database)

    def test_findOneFilter(self):
        filter = UserFilter(username="carmine") #Empty filter
        try:
            userfound = self.service.findOne(filter=filter)
        except UserNotFoundError:
            self.fail(UserNotFoundError.__str__())

        self.assertEqual("carmine",userfound.username)
        #TODO:DEFINE EQUALITY ON OBJECTS USER




