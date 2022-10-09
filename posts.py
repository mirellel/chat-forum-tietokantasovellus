import os
from db import db
from flask import abort, request, session
import users
from datetime import datetime

def create_post(title, content, user_id, topic_id, visibility):
    now = datetime.now()
    time=now.strftime("%d/%m/%Y %H:%M")
    try:
        sql = """INSERT INTO titles (title, content, posted_at, posted_by, topic_id, visibility) 
                VALUES (:title, :content, :posted_at, :posted_by, :topic_id, :visibility)"""
        db.session.execute(sql, {"title":title, "content":content, 
                                "posted_at":time, "posted_by":user_id, "topic_id":topic_id, 
                                "visibility":visibility})
        db.session.commit()
    except:
        return False

    return True

def get_all_posts():
    try:
        sql = """SELECT id, title, content, posted_at, posted_by, topic_id, visibility FROM titles ORDER BY posted_at DESC"""
        result = db.session.execute(sql)
        message = result.fetchall()
        return message
    except:
        return False

def get_title_info(title_id):
    sql = """SELECT t.title, u.username, t.content, t.posted_at 
            FROM titles t, users u WHERE t.id=:title_id AND t.posted_by=u.id"""
    return db.session.execute(sql, {"title_id": title_id}).fetchone()

def delete_title(title_id):
    sql = """UPDATE titles SET visibility=FALSE WHERE id=:id"""
    db.session.execute(sql, {"id":title_id})
    db.session.commit()

    return True
