import os
from unittest import result
from db import db
from flask import abort, request, session
import users
import posts
from datetime import datetime

def create_comment(comment, title_id, username, visibility):
    now = datetime.now()
    time=now.strftime("%d/%m/%Y %H:%M")
    try:
        sql = """INSERT INTO comments (comment, title_id, commentor, sent_at, visibility)
                VALUES (:comment, :title_id, :commentor, :sent_at, :visibility)"""
        db.session.execute(sql, {"comment":comment, "title_id":title_id,
                            "commentor":username, "sent_at":time, "visibility":visibility})
        db.session.commit()

    
    except:
        return False

    return True

def get_comments(title_id):
    try:
        sql = """
            SELECT comment, title_id, commentor, sent_at, visibility, id
            FROM comments
            WHERE title_id=:title_id"""
        result=db.session.execute(sql, {"title_id": title_id}).fetchall()
        return result
    except:
        return False


def delete_comment(comment_id):
    sql = """UPDATE comments SET visibility=FALSE WHERE id=:id"""
    db.session.execute(sql, {"id":comment_id})
    db.session.commit()

    return True