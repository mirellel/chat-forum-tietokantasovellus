import os
from db import db
from flask import abort, request, session
import users

def create_post(title, content, user_id, topic_id, visibility):
    try:
        sql = """INSERT INTO titles (title, content, posted_by, topic_id, visibility) 
                VALUES (:title, :content, :posted_by, :topic_id, :visibility)"""
        db.session.execute(sql, {"title":title, "content":content, 
                                "posted_by":user_id, "topic_id":topic_id, 
                                "visibility":visibility})
        db.session.commit()
    except:
        return False

    return True

def get_all_posts():
    try:
        sql = """SELECT id, title, content, TO_CHAR(posted_at, \'HH24:MI, Mon dd yyyy\'), posted_by, topic_id, visibility FROM titles ORDER BY posted_at DESC"""
        result = db.session.execute(sql)
        message = result.fetchall()
        return message
    except:
        return False

def get_title_info(title_id):
    sql = """SELECT t.title, u.username, t.content, TO_CHAR(t.posted_at, \'HH24:MI, Mon dd yyyy\') 
            FROM titles t, users u WHERE t.id=:title_id AND t.posted_by=u.id"""
    return db.session.execute(sql, {"title_id": title_id}).fetchone()

def delete_title(title_id):
    sql = """UPDATE titles SET visibility=FALSE WHERE id=:id"""
    db.session.execute(sql, {"id":title_id})
    db.session.commit()

    return True

def get_titles_by_topic(topic_id):
    sql = """SELECT id, title, content, TO_CHAR(posted_at, \'HH24:MI, Mon dd yyyy\'), posted_by, topic_id, visibility
            FROM titles
            WHERE topic_id=:topic_id"""
    return db.session.execute(sql, {"topic_id": topic_id}).fetchall()

def get_topics():
    sql = """SELECT id, name FROM topics"""

    return db.session.execute(sql).fetchall()
