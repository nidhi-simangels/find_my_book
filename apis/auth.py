from flask import Blueprint, Response,request,session
import json
from modal.db.connection import connection

auth_app= Blueprint('auth', __name__)

@auth_app.route('/login',methods=['GET'])
def login():
    try:

        data_dict=request.args
        email_id= data_dict.get("email_id")
        password = data_dict.get("password")
        print("email_id",email_id)
        print("password", password)

        query = """
                select email_id,password from d_user where email_id = %(email_id)s and password = %(password)s;
                """

        cursor = connection.engine.execute(query, {"email_id":email_id,"password":password})
        data = cursor.fetchall()

        if len(data)>0:
            body = "successfull login"
            response_data = {"statusCode": 200, "body": body}

        else:
            body = "falied"
            response_data = {"statusCode": 403, "body": body}

        # if email_id=="nidhiranabsc3@gmail.com":
        #
        #     if password=="yesyes":
        #         body = "successfull login"
        #     else:
        #         body = "incorrect password"
        # else:
        #     body =  "incorrect email"
        #

        # response_data = {"statusCode":200,"body":body}
        response = Response(json.dumps(response_data), mimetype='application/json', status=response_data["statusCode"])
        return response
    except Exception as e:
        print("error in login", e)
        response_data = {'status': 500, 'message': 'Internal Server Error ' + str(e)}
        response = Response(json.dumps(response_data), mimetype='application/json', status=response_data["status"])
        return response

