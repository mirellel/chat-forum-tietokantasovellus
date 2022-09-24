import os
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    if not check_password_hash(user[0], password):
        return False
    session["user_id"] = user[1]
    session["username"] = username
    session["csrf_token"] = os.urandom(16).hex()
    return True

def logout():
    del session["user_id"]
    del session["username"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql= """INSERT INTO users (username, password)
                VALUES (:username, :password)"""
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def check_csfr():
    if session["csfr_token"] != request.form["csfr_token"]:
        abort(403)