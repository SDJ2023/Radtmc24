from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  return render_template('index.html')


@app.route("/login")
def login():
  return render_template('login.html')


@app.route("/cancel")
def cancel():
  return render_template('cancel.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
