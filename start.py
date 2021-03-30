from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template("index.html")
   # return "hello world"

@app.route('/biblerc')
def biblerc():
   return "i am in bible rc"


if __name__ == '__main__':
   app.run(debug=True)