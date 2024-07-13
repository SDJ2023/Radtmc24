from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

global myid
global cd
global ss
"""
@app.route("/", methods=['GET', 'POST'])
def cancel():
  myid = request.form.get("rrid")
  cd1 = request.form.get("cd")
  print(myid)
  return render_template("cancel.html", myid=myid, cd=cd1)


@app.route("/index", methods=['GET', 'POST'])
def index():
  #myid=myid
  cd1 = request.form.get("cd")
  d = pd.read_excel("./static/mm.xlsx")
  df = pd.DataFrame(d)
  id = request.form.get("rrid")

  g = df[df['RefNo'] == id]
  g1 = g.to_dict('list')

  print([g1])
  return render_template("index.html", datas=g1, myid=id) """


@app.route('/')
def perform():
  return render_template("perform.html")


@app.route("/result", methods=['POST'])
def result():
  name = request.form['name']
  email = request.form['email']
  message = request.form['message']

  return render_template("result.html",
                         name=name,
                         email=email,
                         message=message)


"""
@app.route("/login")
def login():
  return render_template('login.html')


@app.route("/cancel")
def cancel():
  return render_template('cancel.html')
"""

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
