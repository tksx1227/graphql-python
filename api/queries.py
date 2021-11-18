import logging

from ariadne import convert_kwargs_to_snake_case

from api.models import Post


logger = logging.getLogger(__name__)


def listPosts_resolver(obj, info):
    try:
        posts = [post.to_dict() for post in Post.query.all()]
        payload = {
            "success": True,
            "posts": posts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    logger.info({
        "payload": payload
    })
    return payload


@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        post = Post.query.get(id).to_dict()
        payload = {
            "success": True,
            "post": post
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Post item matching {id} not found"]
        }
    logger.debug({
        "payload": payload
    })
    return payload
