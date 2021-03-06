from celery import Celery

from . import secrets as sec
from .twitter import post_image, get_client
from .images import generate
from .cards import draw_tarot_card

app = Celery('randomwaite.tasks', broker='redis://localhost')

@app.task
def handle_reply(status_id: str, username: str) -> None:
    twitter_client = get_client()
    card = draw_tarot_card()
    im = generate(card)
    text = "@{} {}".format(username, card.name.lower())
    post_image(twitter_client, text, im, reply_to_status_id=status_id)
