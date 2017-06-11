import datetime
import logging

persistenceSettings = {
    "usersCollection" : "user",
    "sensorsCollection" : "sensor",
    "tokensCollection" : "tokens",
    "valueCollection" : "values",
    "dbName" : "tecweb"
}

authSettings = {
    "tokenLifeTime" : datetime.timedelta(minutes=15),
    "adminRole" : 1,
}

