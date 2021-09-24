from flask import Blueprint, Response,request,session
import json
from modal.db.connection import connection

book_app= Blueprint('book_app', __name__)

@book_app.route('/search_book',methods=['GET'])
def search_book():
    try:
        data_dict=request.args
        name= data_dict.get("name")
        if name==None or name.split()=="":
            response_data = {'statusCode':400,"body":"Please provide name"}
        else:
            search_book_resp = connection.search_book(book_name=name)
            if search_book_resp["statusCode"]==200:
                response_data = {"statusCode":200,"body":search_book_resp["body"]}
            else:
                raise Exception("Problem in get_book_summary_resp "+str(search_book_resp) )

        response = Response(json.dumps(response_data), mimetype='application/json', status=response_data["statusCode"])
        return response
    except Exception as e:
        print("error in login", e)
        response_data = {'status': 500, 'message': 'Internal Server Error ' + str(e)}
        response = Response(json.dumps(response_data), mimetype='application/json', status=response_data["status"])
        return response


