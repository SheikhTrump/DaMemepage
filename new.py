###DAmeme page server is unable because the api is not free anymore
from flask import Flask , render_template
import requests
import json

app = Flask(__name__)


def get_meme():
    url = "https://api.memegen.link/templates/"
    response = json . loads(requests.request("GET ,url").text)
    meme_large= response["preview"][-2]
    subreddit=response["subreddit"]
    return meme_large, subreddit


@app.route("/")
def index():
    meme_pic,subreddit = get_meme()
    return render_template("meme_index.html",meme_pic=meme_pic,subreddit=subreddit)
