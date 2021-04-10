from flask import Flask, render_template
import mysql.connector




app = Flask(__name__)

@app.route('/')
def hello_world():
   mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="test"
   )
   mycursor = mydb.cursor()
   mycursor.execute("SELECT * FROM tb1")
   myresult = mycursor.fetchall()
   # myresult=[("val","val"),("val","val")]
   return render_template("index.html", myresult=myresult)
   # return "hello world"

@app.route('/biblerc')
def biblerc():
   return "i am in bible rc"

@app.route('/product/<name>')
def get_product(name):
   mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="test"
   )
   mycursor = mydb.cursor()
   mycursor.execute("""SELECT * FROM tb1 where pk=%s""" % (int(name)))
   myresult = mycursor.fetchall()
   return render_template("article.html", myresult=myresult)


if __name__ == '__main__':
   app.run(debug=True)