from chalice import Chalice
from twython import Twython
import os
from chalicelib import *

app = Chalice(app_name='twitter-demo')

def update_profile_image(image: str):
    twitter = Twython(api_key, api_secret_key, access_token, access_token_secret)
    jpeg_img = open(os.path.join(os.path.dirname(__file__), 'chalicelib/' + image), "rb")
    twitter.update_profile_image(image=jpeg_img)


@app.schedule('cron(0 05 ? * * *)')
def change_to_awake(event):
    update_profile_image('awake.jpeg')


@app.schedule('cron(0 22 ? * * *)')
def change_to_asleep(event):
    update_profile_image('asleep.jpeg')

