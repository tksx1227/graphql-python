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
            created_at=today.strftime("%b-%d-%Y")
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
        "payload": payload
    })
    return payload
