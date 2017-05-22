import functools
from flask_jwt_extended import get_jwt_identity
from flask_restful import abort
from pymongo import MongoClient
from common.utils.auth import AuthManager

def is_admindecorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        useridentity = get_jwt_identity()

        if AuthManager(MongoClient().tecweb).is_admin(useridentity):
            return func(*args, **kwargs)

        abort(401)

    return wrapper