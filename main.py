from flask import Flask, request,Response
import json
from modal.db.connection import connection
from apis.auth import  auth_app
from apis.summary import  summary_app

app = Flask(__name__)

app.register_blueprint(auth_app)
app.register_blueprint(summary_app)



# getbook
#
# get genre
#
# login
#
# your fav book
#
# add your fav book
#
# rate the book
#
# books_summary
# book id
# such that number of comment
# number of genre
# how many person like this book
# how many person rated
# what is avg rating out of 5
# how many person  add fav this book





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
