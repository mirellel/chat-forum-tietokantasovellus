from crypt import methods
from app import app
from flask import render_template, request, redirect
import users
import posts

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

		if not users.login(username, password):
			return render_template("error.html", message="Väärä tunnus tai salasana!")
		return redirect("/")

@app.route("/logout")
def logout():
	users.logout()
	return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username)<1 or len(username)>20:
            return render_template("error.html", message="Tunnuksessa tulee olla 1-20 merkkiä")

        if " " in username:
            return render_template("error.html", message="Tunnuksessa ei saa olla välilyöntejä")

        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if password1 != password2:
            return render_template("error.html", message="Salasanat eivät täsmää")

        if password1 == "":
            return render_template("error.html", message="Salasana on tyhjä")

        if " " in password1:
            return render_template("error.html", message="Salasanassa ei saa olla välilyöntejä")

        role = request.form["role"]
        if role not in ("1", "2"):
            return render_template("error.html", message="Tuntematon käyttäjärooli")
        
        if not users.register(username, password1, role):
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        return redirect("/")

@app.route("/create", methods=["GET", "POST"])
def new_title():
    if request.method =="GET":
        return render_template("create.html")

    if request.method == "POST":
        return redirect("/")

@app.route("/new", methods=["GET", "POST"])
def created():
    if request.method == "GET":
        return render_template("new.html")
    if request.method == "POST":
        title = request.form["title"]
        comment = request.form["comment"]
        id=request.form["user_id"]
        topic=request.form["topic"]
        if title == "":
            return render_template("error.html", message="Otsikko ei saa olla tyhjä!")
        if comment == "" or  comment == "    ":
            return render_template("error.html", message="Aloituskommentti ei saa olla tyhjä!")
        if not posts.create_post(title, comment, id, topic, True):
            return render_template("error.html", message="Postauksen luonti ei onnistunut")

        return redirect("/")
