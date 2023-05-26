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
            VALUES (:name, :address, :description)"""
    db.session.execute(text(sql), {"name":name, "address":address, "description":description})
    db.session.commit()

def add_opening_hours(place_id, weekday, opens, closes):
    sql = """INSERT INTO openinghours (exerciseplaces_id, weekday, opens, closes)
            VALUES (:exerciseplaces_id, :weekday, :opens, :closes)"""
    db.session.execute(text(sql),
                       {"exerciseplaces_id":place_id, "weekday":weekday, "opens":opens, "closes": closes})
    db.session.commit()

def update_places(place_id, name, address, description):
    sql = """UPDATE exerciseplaces SET name=:name, address=:address, description=:description
            WHERE id=:place_id"""
    db.session.execute(text(sql),
                       {"name":name, "address":address, "description":description, "place_id":place_id})
    db.session.commit()

def add_review(place_id, user_id, stars, review):
    sql = """INSERT INTO reviews (exerciseplaces_id, user_id, stars, review, time)
            VALUES (:exerciseplaces_id, :user_id, :stars, :review, NOW())"""
    db.session.execute(text(sql),
                       {"exerciseplaces_id":place_id, "user_id":user_id, "stars":stars,
                        "review":review})
    db.session.commit()
