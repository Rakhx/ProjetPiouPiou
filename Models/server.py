from flask import Flask
from markupsafe import escape
from flask import url_for

from ProjectPiouPiou.Models.MoteurFlask import MoteurFlask

app = Flask(__name__)
letsgo = MoteurFlask()


@app.route("/land")
def getTailleTerrain():
    return "50x50"

def deplacementUnite(name, position):
    pass
@app.route('/login')
def login():
    letsgo.incValue()
    valeur = letsgo.getValue()
    return str(valeur)

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='JohnDoe'))

