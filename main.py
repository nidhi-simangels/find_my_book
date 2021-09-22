from flask import Flask,request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/nidhi')
def hello_world1():
    return render_template('front.html')


@app.route('/login',methods=["POST"])
def checkLogin():
     UN = request.form['username']
     PS = request.form['password']

     sqlconnection = sqlite3.connection(currentlocation +"\login.db")
     cursor =  sqlconnection.cursor()
     query1="select username ,password from users WHERE username={un} and password={ps}".format(un=UN,ps=PS)
     rows = cursor.execute(query1)
     rows = rows.fetchall()
     if len(rows)==1:
         return "frontend"
     else:
         return "not to attendpage"



if __name__ == '__main__':
    app.run()
