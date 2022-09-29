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
