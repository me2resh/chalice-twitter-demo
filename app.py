from chalice import Chalice
from twython import Twython
import os
from chalicelib import *

app = Chalice(app_name='twitter-demo')

def update_profile_image(image: str):
    twitter = Twython(api_key, api_secret_key, access_token, access_token_secret)
    jpeg_img = open(os.path.join(os.path.dirname(__file__), 'chalicelib/' + image), "rb")
    twitter.update_profile_image(image=jpeg_img)


@app.route('/awake')
def change_to_awake():
    update_profile_image('awake.jpeg')
    return 'Awake!'


@app.route('/asleep')
def change_to_asleep():
    update_profile_image('asleep.jpeg')
    return 'Asleep!'

