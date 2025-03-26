from flask import Flask , render_template
import requests
import json

app = Flask(__name__)
app.config['DEBUG'] = True




@app.route("/")
def index():
   return "<h1>Change </h1>"

@app.route('/hello')
def hello():
    return 'Hello, World'