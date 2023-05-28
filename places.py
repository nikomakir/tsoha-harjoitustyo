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

def add_place(name, address, description, monday, tuesday, wednesday,
              thursday, friday, saturday, sunday):
    sql = """INSERT INTO exerciseplaces (name, address, description, monday, tuesday,
            wednesday, thursday, friday, saturday, sunday)
            VALUES (:name, :address, :description, :monday, :tuesday, :wednesday,
            :thursday, :friday, :saturday, :sunday)"""
    db.session.execute(text(sql), {"name":name, "address":address, "description":description,
                                   "monday":monday, "tuesday":tuesday, "wednesday":wednesday,
                                   "thursday":thursday, "friday":friday, "saturday":saturday,
                                   "sunday":sunday})
    db.session.commit()

def update_place(updates, place_id):
    for update, new in updates.items():
        sql = "UPDATE exerciseplaces SET :update=:value WHERE id=:place_id"
        db.session.execute(text(sql), {"update":update, "value":new, "place_id":place_id})
    db.session.commit()

def get_place_info(place_id):
    sql = """SELECT name, address, description, monday, tuesday,
            wednesday, thursday, friday, saturday, sunday
            FROM exerciseplaces WHERE id=:place_id"""
    return db.session.execute(text(sql), {"place_id":place_id}).fetchone()

def add_review(place_id, user_id, stars, review):
    sql = """INSERT INTO reviews (exerciseplaces_id, user_id, stars, review, time)
            VALUES (:exerciseplaces_id, :user_id, :stars, :review, NOW())"""
    db.session.execute(text(sql),
                       {"exerciseplaces_id":place_id, "user_id":user_id, "stars":stars,
                        "review":review})
    db.session.commit()

def get_reviews(place_id):
    sql = """SELECT stars, review, user_id, time FROM reviews
            WHERE exerciseplaces_id=:id ORDER BY time DESC"""
    return db.session.execute(text(sql), {"id":place_id}).fetchall()

def create_groupname(name):
    sql = "INSERT INTO groupnames (name) VALUES (:name)"
    try:
        db.session.execute(text(sql), {"name":name})
        db.session.commit()
        return True
    except:
        return False

def add_place_to_group(place_id, groupname):
    sql = """INSERT INTO groups (exerciseplaces_id, groupnames_id)
            VALUES (:place_id, :groupname)"""
    try:
        db.session.execute(text(sql), {"place_id":place_id, "groupname":groupname})
        db.session.commit()
        return True
    except:
        return False
