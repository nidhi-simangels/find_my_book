import jwt
import config
import datetime
from flask import request,Response
import json

def createToken(user_id):
    token = jwt.encode({'user_id' : user_id,'exp' : datetime.datetime.utcnow()+ datetime.timedelta(minutes=config.SESSION_OUT_MINUTES) }, config.jwt_token_Key)
    return token.decode('utf-8')


def authenticate_token(auth_token):
    try:
        auth_token = auth_token.split(' ')[-1]
        payload = jwt.decode(auth_token, config.jwt_token_Key)
        if payload:
            return {"token_ok": True, "payload": payload}
    except Exception as e:
        print('exception logged',e)
        return {"token_ok": False}


def get_user_id(auth_token):
    auth_response = authenticate_token(auth_token=auth_token)
    if auth_response['token_ok']:
        payload = auth_response['payload']
        user_obj_id = payload['user_id']
        return user_obj_id
    else:
        return None


def login_decorator(func):   #decorator ;-)
    def inner():
        #### decorating part ####
        # user_token=request.headers.get('Authorization')

        user_token = request.args.get('token')
        if user_token ==None  :
            data = {"message": "You forget to add Token.", "status": 401}
            return Response(json.dumps(data), mimetype='application/json', status=401)

        else:
            user_id = get_user_id(user_token)
            if user_id:
                return func(user_id=user_id)
            else:
                data = {"message": "Your session has expired", "status": 401}
                return Response(json.dumps(data), mimetype='application/json', status=401)

    inner.__name__=func.__name__
    return inner

