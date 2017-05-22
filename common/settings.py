import datetime

persistenceSettings = {
    "usersCollection" : "user",
    "sensorsCollection" : "sensor",
    "tokensCollection" : "tokens",
    "dbName" : "tecweb"
}

authSettings = {
    "tokenLifeTime" : datetime.timedelta(minutes=15),
    "adminRole" : 1,
}
