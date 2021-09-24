from flask import Blueprint, Response,request,session
import json
from modal.db.connection import connection
from modal.authentication.jwt_services import login_decorator

user_app= Blueprint('user_app', __name__)

@user_app.route('/user_favorite_books',methods=['GET'])
@login_decorator
def user_favorite_books(user_id):
    try:
        get_user_favorite_resp = connection.get_user_favorite(user_id=user_id)

        if get_user_favorite_resp["statusCode"]==200:
            response_data = {"statusCode":200,"body":get_user_favorite_resp["body"]}
        else:
            raise Exception("Problem in get_user_favorite_resp "+str(get_user_favorite_resp) )

        response = Response(json.dumps(response_data), mimetype='application/json', status=response_data["statusCode"])
        return response
    except Exception as e:
        print("error in login", e)
        response_data = {'status': 500, 'message': 'Internal Server Error ' + str(e)}
        response = Response(json.dumps(response_data), mimetype='application/json', status=response_data["status"])
        return response





