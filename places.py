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
            :thursday, :friday, :saturday, :sunday) RETURNING id"""

    result = db.session.execute(text(sql), {"name":name, "address":address, "description":description,
                                   "monday":monday, "tuesday":tuesday, "wednesday":wednesday,
                                   "thursday":thursday, "friday":friday, "saturday":saturday,
                                   "sunday":sunday})
    place_id = result.fetchone()[0]
    db.session.commit()
    return place_id

def update_place(place_id, name, address, description,
                 monday, tuesday, wednesday, thursday,
                 friday, saturday, sunday):
    sql = """UPDATE exerciseplaces SET name=:name, address=:address,
            description=:description, monday=:monday, tuesday=:tuesday,
            wednesday=:wednesday, thursday=:thursday, friday=:friday,
            saturday=:saturday, sunday=:sunday
            WHERE id=:place_id"""

    db.session.execute(text(sql), {"name":name, "address":address, "description":description,
                                   "monday":monday, "tuesday":tuesday, "wednesday":wednesday,
                                   "thursday":thursday, "friday":friday, "saturday":saturday,
                                   "sunday":sunday, "place_id":place_id})
    db.session.commit()

def get_place_info(place_id):
    sql = """SELECT id, name, address, description, monday, tuesday,
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
    sql = """SELECT u.username, r.stars, r.review, r.time FROM reviews r, users u
            WHERE r.exerciseplaces_id=:id AND r.user_id=u.id ORDER BY r.time DESC"""
    return db.session.execute(text(sql), {"id":place_id}).fetchall()

def create_groupname(name):
    sql = "INSERT INTO groupnames (name) VALUES (:name)"
    try:
        db.session.execute(text(sql), {"name":name})
        db.session.commit()
        return True
    except:
        return False

def get_groupnames():
    sql = "SELECT id, name FROM groupnames ORDER BY name"
    return db.session.execute(text(sql)).fetchall()

def add_place_to_group(place_id, groupname_id):
    sql = """INSERT INTO groups (exerciseplaces_id, groupnames_id)
            VALUES (:place_id, :groupnames_id)"""
    try:
        db.session.execute(text(sql), {"place_id":place_id, "groupnames_id":groupname_id})
        db.session.commit()
    except:
        pass

def get_groups(place_id):
    sql = """SELECT n.id, n.name FROM groupnames n, groups g
            WHERE n.id=g.groupnames_id AND g.exerciseplaces_id=:place_id
            ORDER BY n.name"""
    return db.session.execute(text(sql), {"place_id":place_id}).fetchall()

def remove_from_group(place_id, group_id):
    sql = "DELETE FROM groups WHERE exerciseplaces_id=:place_id AND groupnames_id=:group_id"
    db.session.execute(text(sql), {"place_id":place_id, "group_id":group_id})
    db.session.commit()
