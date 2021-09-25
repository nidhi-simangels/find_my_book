from flask import Blueprint, Response,request,session
import json
from modal.db.connection import connection

summary_app= Blueprint('summary_app', __name__)

@summary_app.route('/book_summary',methods=['GET'])
def book_summary():
    try:
        data_dict=request.args
        page_id= int(data_dict.get("page_id",default=1))
        limit  = int(data_dict.get("limit",default=10))

        get_book_summary_resp = connection.get_book_summary(page_id=page_id,limit=limit)

        if get_book_summary_resp["statusCode"]==200:
            response_data = {"statusCode":200,"body":get_book_summary_resp["body"]}
        else:
            raise Exception("Problem in get_book_summary_resp "+str(get_book_summary_resp) )

        response = Response(json.dumps(response_data), mimetype='application/json', status=response_data["statusCode"])
        return response
    except Exception as e:
        print("error in login", e)
        response_data = {'status': 500, 'message': 'Internal Server Error ' + str(e)}
        response = Response(json.dumps(response_data), mimetype='application/json', status=response_data["status"])
        return response


