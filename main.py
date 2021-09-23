from flask import Flask, request,Response
import json
from modal.db.connection import connection
app = Flask(__name__)


@app.route('/')
def hello_world():
    cursor = connection.engine.execute("select name from d_book")
    data=cursor.fetchall()
    list_name =[]
    for i in data:
       list_name.append(i[0])

    response_data = {"status": 200, "message": list_name}
    return Response(json.dumps(response_data),mimetype='application/json',status=response_data["status"])



if __name__ == '__main__':
    app.run()
