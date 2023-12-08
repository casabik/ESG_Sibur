from typing import Union
from fastapi import APIRouter
from models import Comments
from peewee import fn

router = APIRouter()

@router.get("/get_comments")
def get_comments(user_text: str):
    comments = Comments.select().where(fn.Match(Comments.text, fn.tsquery(user_text)))
                                       
    data = []
    for comment in comments:
        dict = {"comment_id": comment.comment_id, "person_id": comment.person_id, "date": comment.date, "text": comment.text, "parents_stack": comment.parents_stack, "post_id": comment.post_id, "likes": comment.likes}
        data.append(dict)

    if len(comments) == 0:
        return {"message": "Not found"}
    return {"message": "Found", "comments": data}