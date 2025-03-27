from flask import Flask , render_template
import requests
import json

app = Flask(__name__)
app.config['DEBUG'] = True




@app.route("/")
def index():
   return render_template("home.html")
'''
@app.route('/hello')
def hello():
    return 'Hello, World'



@app.route('/about/<username>')
def about(username):
    return f'<h1>HEllo from ABOUT {username} </h1>'

'''
@app.route("/market")
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template("market.html",items=items)