from flask import Flask, render_template,redirect,url_for,flash,request
from sqlalchemy import *
import psycopg2
from models.models import Database


app = Flask(__name__)
app.secret_key = 'some_secret'



@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/ADD RECORD',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         fathername = request.form['fathername']
         email = request.form['email']
         address = request.form['address']
         schoolname = request.form['schoolname']


         #change user and password according to platform
         engine = create_engine('postgres://postgres:anojk@localhost:5432/schoolapp')
         Database.metadata.create_all(engine)
         conn = engine.connect()
         ins = Database.student.insert()
         conn.execute(ins, student_name=request.form['name'],father_name=request.form['fathername'], email=request.form['email'],address=request.form['address'],school_name=request.form['schoolname'])
         return render_template("result.html")

      except:
        return render_template("resultnot.html")


@app.route('/Show Record', methods = ['POST', 'GET'])
def show_all():
    try:

        squery = Database.conn.execute("select * from student").fetchall()
        print(squery)
        return render_template('show_all.html',squery=squery)

    except:
        return render_template("resultnot.html")


if __name__ == '__main__':
    app.run(debug=True)
