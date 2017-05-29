from unittest import TestCase
from pymongo import MongoClient
import datetime
import dateutil.parser
from common.models.user import User
from common.models.value import Value
from common.models.sensor import Sensor
from common.models.project import Project
from common.services.userservice import UserService
from common.services.sensors import SensorService
from common.services.values import ValueService
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

"""
class TestUserService(TestCase):
    def setUp(self):
        self.database = MongoClient().tecweb
        self.service = UserService(self.database)

    def test_delete(self):
        deletefilter = UserFilter(id="")
        try:
            self.service.delete(deletefilter)
        except UserNotFoundError as e:
            self.fail(e)
        print("Delete test passed \n")

    def test_findFilter(self):
        filter = UserFilter(username="carmine") #Empty filter
        expecteduser = User(id="591ff8f647488822d7b707d4",username="carmine",password="ciao",role=1,email="carmine.dimonaco@gmail.com")
        try:
            userfound = self.service.find(filter=filter)
        except UserNotFoundError as e:
            self.fail(e)
        print(expecteduser)
        print(userfound[0])
        self.assertTrue(userfound[0].__eq__(expecteduser))


    def test_adduser(self):
        testuser = User(username="test",password="test",role=0,email="test@email.com")
        try:
            insertedid = self.service.add(testuser)
        except UserAddError as e:
            self.fail(e)
        print(insertedid)

"""


class TestSensorService(TestCase):
    def setUp(self):
        self.database = MongoClient().tecweb
        self.service = SensorService(self.database)

    """def test_addsensor(self):
        testsensor = Sensor(name="Testsensor",apikey="8598984908092083098093",project="591ff9458e2b82f3872c111b")
        try:
            insertedid = self.service.add(testsensor)
        except SensorAddError as e:
            self.fail(e)
        print(insertedid)"""

    """def test_findsensor(self):
        filter = SensorFilter(id="5921ceef47488822d7b72931")
        expectedsensor = Sensor(id="5921ceef47488822d7b72931",name="Temperatura 04",project="591ff9458e2b82f3872c111b",apikey="870968098489084509854")
        try:
            sensorfound = self.service.find(filter=filter)
        except SensorNotFoundError as e:
            self.fail(e)
        print(expectedsensor)
        print(sensorfound[0])

        self.assertTrue(sensorfound[0].__eq__(expectedsensor))"""

    """def test_findsensorpagination(self):
        filter = SensorFilter()
        hasmore = True
        offset = 0
        limit = 10
        while hasmore:
            sensorfound,hasmore = self.service.find(filter=filter,offset=offset)
            offset = offset + limit
            print(len(sensorfound),hasmore)"""



    """
    def test_deletesensor(self):
        deletefilter = SensorFilter(id="5921b904ef43d217544829d1")
        try:
            self.service.delete(deletefilter)
        except SensorNotFoundError as e:
            self.fail(e)

    def test_addvalue(self):
        testvalue = Value(value=9898,timestamp=datetime.datetime.now(),additional="TEST")
        try:
            insertedid = self.service.setvalue(sensorid="5921e8f8ef43d21ea51a29e6",value=testvalue)
        except ValueAddError as e:
            self.fail(e)

        print(insertedid)

    def test_getvalues(self):
        expectedvalue = Value(value=893.288,timestamp=dateutil.parser.parse("2016-04-01T10:30:36.438Z"),additional="",id="591ffa1d8e2b82f3872c111c")
        timefilter = TimeFilter(timeto=datetime.datetime.now())
        print(timefilter.getConditions())
        filter = ValueFilter(id="5921cf1824dcb4b5f1caf42d",timestamp=timefilter) #TODO:ADD COMPARISON TO EXPECTED VALUE BUT TEST WORKS
        try:
            values = self.service.getvalues(filter=filter)
        except ValueNotFoundError as e:
            self.fail(e)

        print(values[0])

    def test_resetsensor(self):
        try:
            self.service.resetvalues(sensorid="5921e8f8ef43d21ea51a29e6")
        except SensorNotFoundError as e:
            self.fail(e)

"""

"""class TestProjectService(TestCase):
    def setUp(self):
        self.database = MongoClient().tecweb
        self.service = ProjectService(self.database)

    def test_addproject(self):
        projecttoadd = Project(name="Test",description="Test description",createdAt=datetime.datetime.now())
        try:
            insertedid = self.service.add(userid="591ff8f647488822d7b707d4",project=projecttoadd)
        except ProjectAddError as e:
            self.fail(e)

        print(insertedid)

    def test_findproject(self):
        filter = ProjectFilter(id="591ff8f647488822d7b707d4")
        try:
            projects = self.service.find(filter=filter)
        except ProjectNotFoundError:
            self.fail(ProjectNotFoundError)

    def test_deleteproject(self):
        try:
            self.service.delete(projectid="5921fad7ef43d22441866504",userid="591ff8f647488822d7b707d4")
        except (ProjectNotFoundError,SensorNotFoundError) as e:
            self.fail(e)

"""
import datetime
class TestValueService(TestCase):

    def setUp(self):
        self.database = MongoClient().tecweb
        self.service = ValueService(self.database)

    def test_addvalue(self):
        now = datetime.datetime.now()
        onehour = now - datetime.timedelta(hours=1)
        twohour = now - datetime.timedelta(hours=2)
        threehour = now - datetime.timedelta(hours=3)
        fourhour = now - datetime.timedelta(hours=4)
        fivehour = now - datetime.timedelta(hours=5)
        sixhour = now - datetime.timedelta(hours=6)
        newvalue = Value(value=899,timestamp=now,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)
        newvalue = Value(value=678,timestamp=now,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)
        newvalue = Value(value=876,timestamp=onehour,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)
        newvalue = Value(value=234,timestamp=onehour,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)
        newvalue = Value(value=256,timestamp=twohour,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)
        newvalue = Value(value=987,timestamp=twohour,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)
        newvalue = Value(value=123,timestamp=threehour,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)
        newvalue = Value(value=34,timestamp=threehour,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)
        newvalue = Value(value=12,timestamp=fourhour,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)
        newvalue = Value(value=34,timestamp=fourhour,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)
        newvalue = Value(value=1,timestamp=fivehour,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)
        newvalue = Value(value=23,timestamp=fivehour,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)
        newvalue = Value(value=344,timestamp=sixhour,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)
        newvalue = Value(value=12,timestamp=sixhour,sensorid="592af67aef43d2029ea7b35a")
        insertedid = self.service.add(newvalue)
        print(insertedid)

    """def test_findvaluespagination(self):
          filter = ValueFilter(sensorid="5921e8f8ef43d21ea51a29e6")
          hasmore = True
          offset = 0
          limit = 100
          while hasmore:
              sensorfound,hasmore = self.service.find(filter=filter,offset=offset)
              offset = offset + limit
              print(len(sensorfound),hasmore)


    def test_deletevalue(self):
        filter = ValueFilter()
        self.service.delete(filter)"""

