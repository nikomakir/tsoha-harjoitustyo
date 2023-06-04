from sqlalchemy.sql import text
from db import db


def place_list():
    sql = "SELECT id, name FROM exerciseplaces ORDER BY id"
    return db.session.execute(text(sql)).fetchall()

def place_rankings():
    sql = """SELECT p.id, p.name, COALESCE((SELECT AVG(stars) FROM reviews
            WHERE exerciseplaces_id=p.id), 0) r
            FROM exerciseplaces p GROUP BY p.id ORDER BY r DESC"""
    return db.session.execute(text(sql)).fetchall()

def find_all_by_word(word):
    sql = """SELECT id, name, description FROM exerciseplaces
            WHERE description LIKE :query OR name LIKE :query"""
    return db.session.execute(text(sql), {"query":"%"+word+"%"}).fetchall()
