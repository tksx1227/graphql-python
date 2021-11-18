import logging
from datetime import datetime

from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Post


logger = logging.getLogger(__name__)


@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, title, description):
    try:
        today = datetime.today()
        post = Post(
            title=title,
            description=description,
            created_at=today.date()
        )
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [
                "Incorrect date format provided. Date should be in the format dd-mm-yyyy"
            ]
        }
    logger.debug({
        "type": "create",
        "payload": payload
    })
    return payload


@convert_kwargs_to_snake_case
def update_post_resolver(obj, info, id, title, description):
    try:
        post = Post.query.get(id)
        if post:
            post.title = title
            post.description = description
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"item matching id {id} not found"]
        }
    logger.debug({
        "type": "update",
        "payload": payload
    })
    return payload


@convert_kwargs_to_snake_case
def delete_post_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except Exception:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    logger.debug({
        "type": "delete",
        "payload": payload
    })
    return payload
