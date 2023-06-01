import os
from flask import request, session, abort
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from db import db


def login(name, password):
    sql = "SELECT id, password, role FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":name}).fetchone()
    if not result:
        return False
    if not check_password_hash(result.password, password):
        return False
    session["user_id"] = result[0]
    session["user_name"] = name
    session["user_role"] = result[2]
    session["csrf_token"] = os.urandom(16).hex()
    return True

def logout():
    del session["user_id"]
    del session["user_name"]
    del session["user_role"]

def register(name, password, role):
    hash_value = generate_password_hash(password)
    try:
        sql = """INSERT INTO users (username, password, role)
                VALUES (:name, :password, :role)"""
        db.session.execute(text(sql), {"name":name, "password":hash_value, "role":role})
        db.session.commit()
    except:
        return False
    return login(name, password)

def user_id():
    return session.get("user_id", 0)

def require_role(role):
    if role > session.get("user_role", 0):
        abort(403)

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
