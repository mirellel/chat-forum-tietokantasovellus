import os
from unittest import result
from db import db
from flask import abort, request, session
import users
import posts

def create_comment(comment, title_id, username, visibility):
    try:
        sql = """INSERT INTO comments (comment, title_id, commentor, visibility)
                VALUES (:comment, :title_id, :commentor, :visibility)"""
        db.session.execute(sql, {"comment":comment, "title_id":title_id,
                            "commentor":username, "visibility":visibility})
        db.session.commit()

    
    except:
        return False

    return True

def get_comments(title_id):
    try:
        sql = """
            SELECT comment, title_id, commentor, TO_CHAR(sent_at, \'HH24:MI, Mon dd yyyy\') visibility, id
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