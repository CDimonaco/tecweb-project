from flask import Flask,request,jsonify
import logging
import datetime
from pymongo import MongoClient
import simplekv.db.mongo
from flask_bcrypt import Bcrypt
from common.utils.auth import AuthManager
from flask_restful import Api,abort
from common.models.user import User
from common.models.sensor import Sensor
from resources.auth import AuthLogin,AuthLogout
from flask_jwt_extended import JWTManager, jwt_required, \
    get_jwt_identity, revoke_token, unrevoke_token, \
    get_stored_tokens, get_all_stored_tokens, create_access_token, \
    create_refresh_token, jwt_refresh_token_required, \
    get_raw_jwt, get_stored_token

import functools

mongoClient = MongoClient()
mongoDatabase = mongoClient["tecweb"]
authManager = AuthManager(database=mongoDatabase)
app = Flask(__name__)
api = Api(app=app)
app.secret_key = "sosecretlol"
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_STORE'] = simplekv.db.mongo.MongoStore(db=mongoDatabase,collection="tokens")
# Check all tokens (access and refresh) to see if they have been revoked.
# You can alternately check only the refresh tokens here, by setting this
# to 'refresh' instead of 'all'
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = 'all'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=5)
#Create mongodb client and connect to the database "tecweb"
f_bcrypt = Bcrypt(app)
#Log setup
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

jwt = JWTManager(app)

"""
# Standard login endpoint
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not authManager.login(username=username,password=password):
        return jsonify({"msg": "Bad username or password"}), 401
    ret = {
        'access_token': create_access_token(identity=username),
    }
    return jsonify(ret), 200

# Helper method to revoke the current token used to access
# a protected endpoint
def _revoke_current_token():
    current_token = get_raw_jwt()
    jti = current_token['jti']
    revoke_token(jti)

# Endpoint for revoking the current users access token
@app.route('/logout', methods=['POST'])
@jwt_required
def logout():
    try:
        authManager.logout(get_raw_jwt())
    except KeyError:
        return jsonify({
            'msg': 'Access token not found in the blacklist store'
        }), 500
    return jsonify({"msg": "Successfully logged out"}), 200


@app.route('/')
def hello_world():
    app.logger.debug("HERE")
    app.logger.info("INFO")
    return 'Hello World!'

@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    return jsonify({'hello': 'world'})
"""





api.add_resource(AuthLogin,"/auth/login",resource_class_kwargs={ 'auth_manager': authManager })
api.add_resource(AuthLogout,"/auth/logout",resource_class_kwargs={ 'auth_manager': authManager })
if __name__ == '__main__':
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(consoleHandler)
    app.run()
