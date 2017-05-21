from unittest import TestCase
from pymongo import MongoClient
import datetime
from common.models.user import User
from common.models.value import Value
from common.models.sensor import Sensor
from common.models.value import Value
from common.services.userservice import UserService
from common.services.sensors import SensorService
from common.services.projects import ProjectService
from common.filters.users import UserFilter
from common.filters.projects import ProjectFilter
from common.filters.sensors import SensorFilter
from common.filters.values import ValueFilter
from common.filters.time import TimeFilter
from common.exceptions.users import UserNotFoundError,UserAddError
from common.exceptions.sensors import SensorNotFoundError,SensorAddError
from common.exceptions.values import ValueAddError,ValueNotFoundError
from common.exceptions.project import ProjectNotFoundError,ProjectAddError

class TestUserService(TestCase):
    def setUp(self):
        self.database = MongoClient().tecweb
        self.service = UserService(self.database)

    """def test_delete(self):
        deletefilter = UserFilter(id="")
        try:
            self.service.delete(deletefilter)
        except UserNotFoundError:
            self.fail(UserNotFoundError)
        print("Delete test passed \n")"""

    def test_findFilter(self):
        filter = UserFilter(username="carmine") #Empty filter
        expecteduser = User(id="591ff8f647488822d7b707d4",username="carmine",password="ciao",role=1,email="carmine.dimonaco@gmail.com")
        try:
            userfound = self.service.find(filter=filter)
        except UserNotFoundError:
            self.fail(UserNotFoundError)
        print(expecteduser)
        print(userfound[0])
        self.assertTrue(userfound[0].__eq__(expecteduser))


    def test_adduser(self):
        testuser = User(username="test",password="test",role=0,email="test@email.com")
        try:
            insertedid = self.service.add(testuser)
        except UserAddError:
            self.fail(UserAddError)
        print(insertedid)




class TestSensorService(TestCase):
    def setUp(self):
        self.database = MongoClient().tecweb
        self.service = SensorService(self.database)

    def test_addsensor(self):
        testsensor = Sensor(name="Testsensor",apikey="8598984908092083098093",project="591ff9458e2b82f3872c111b")
        try:
            insertedid = self.service.add(testsensor)
        except SensorAddError:
            self.fail(SensorAddError)
        print(insertedid)

    def test_findsensor(self):
        filter = SensorFilter(id="591ffa3547488822d7b70813")
        expectedsensor = Sensor(id="591ffa3547488822d7b70813",name="Temperatura 01",project="591ff9458e2b82f3872c111b",apikey="abcdefghilmnopqrstuvz1245")
        try:
            sensorfound = self.service.find(filter=filter)
        except SensorNotFoundError:
            self.fail(SensorNotFoundError)
        print(expectedsensor)
        print(sensorfound[0])

        self.assertTrue(sensorfound[0].__eq__(expectedsensor))

    """def test_deletesensor(self):
        deletefilter = SensorFilter(id="5921b904ef43d217544829d1")
        try:
            self.service.delete(deletefilter)
        except SensorNotFoundError:
            self.fail(SensorNotFoundError)"""

    def test_addvalue(self):
        testvalue = Value(value=9898,timestamp=datetime.datetime.now(),additional="TEST")
        try:
            insertedid = self.service.setvalue(sensorid="591ffa3547488822d7b70813",value=testvalue)
        except ValueAddError:
            self.fail(ValueAddError)

        print(insertedid)

