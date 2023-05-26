from sqlalchemy.sql import text
from db import db


def delete_review(review_id):
    sql = "DELETE FROM reviews WHERE id=:id"
    db.session.execute(text(sql), {"id":review_id})
    db.session.commit()

def delete_place(place_id):
    sql = "DELETE FROM exerciseplaces WHERE id=:id"
    db.session.execute(text(sql), {"id":place_id})
    db.session.commit()

def add_place(name, address, description):
    sql = """INSERT INTO exerciseplaces (name, address, description)
            VALUES (name:name, address:address, description:description)"""
    db.session.execute(text(sql), {"name":name, "address":address, "description":description})
    db.session.commit()




