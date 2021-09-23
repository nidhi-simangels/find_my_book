from flask import Flask, request,Response
import json
from modal.db.connection import connection
from apis.auth import  auth_app

app = Flask(__name__)

app.register_blueprint(auth_app)



@app.route('/')
def hello():
    response_data = {"statusCode": 200, "body":"hello from find_my_book" }
    return Response(json.dumps(response_data),mimetype='application/json',status=response_data["statusCode"])

#
# @app.route('/')
# def hello():
#     cursor = connection.engine.execute("select name from d_book")
#     data=cursor.fetchall()
#     list_name =[]
#     for i in data:
#        list_name.append(i[0])
#
#     response_data = {"status": 200, "message": list_name}
#     return Response(json.dumps(response_data),mimetype='application/json',status=response_data["status"])



if __name__ == '__main__':
    app.run()
