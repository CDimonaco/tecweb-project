from unittest import TestCase
from pymongo import MongoClient
from .userservice import UserService
from ..filters.users import UserFilter
from ..exceptions.users import UserNotFoundError,UserAddError

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





