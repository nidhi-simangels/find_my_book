from flask import Blueprint, Response,request,session
import json

auth_app= Blueprint('auth', __name__)

@auth_app.route('/login',methods=['GET'])
def login():
    try:
        print(request.args.get("email_id"))
        response_data = {"statusCode":200,"body":"Login Successfull"}
        response = Response(json.dumps(response_data), mimetype='application/json', status=response_data["statusCode"])
        return response
    except Exception as e:
        print("error in login", e)
        response_data = {'status': 500, 'message': 'Internal Server Error ' + str(e)}
        response = Response(json.dumps(response_data), mimetype='application/json', status=response_data["status"])
        return response

