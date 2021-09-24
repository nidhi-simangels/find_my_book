import jwt
import config
import datetime


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

