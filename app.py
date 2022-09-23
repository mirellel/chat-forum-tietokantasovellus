from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login",methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
	session["username"] = username
	return redirect("/")
@app.route("/logout")
def logout():
	del session["username"]
	return redirect("/")

