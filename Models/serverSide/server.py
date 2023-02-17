from threading import Lock
from flask import Flask, request
from ProjectPiouPiou.Models.serverSide.MoteurFlask import MoteurFlask


# --------------------------------------
#   Element autre de la classe
# --------------------------------------
app = Flask(__name__)
moteur = MoteurFlask()
lock = Lock()

def convertToString(value):
    return [tuple(str(x) for x in value)]


# --------------------------------------
#   Initialisation de début de game
# --------------------------------------

# Register le nom de la team, return la position du drapeau de départ
@app.route("/init/register/<name>")
def registerTeam(name):
    return convertToString(moteur.registerTeam(name))

# Taille du terrain
@app.route("/init/land")
def getTailleTerrain():
    return [tuple(str(x) for x in moteur.getTailleMap())]

# Unités disponibles pour préparation
@app.route("/init/units")
def getAvailableUnit():
    return moteur.getStartUnite()


@app.route("/init/register", methods=['GET'])
def registerUnit():
    test = request.args.to_dict()
    return moteur.registerUnite(test["team"],test["type"],test["name"],test["posX"], test["posY"])


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


# --------------------------------------
#   Boucle en cours de  game
# --------------------------------------
def deplacementUnite(name, position):
    pass

# --------------------------------------
# Mutex stuff
# --------------------------------------

@app.route('/askPrio')
def getPriority():
    lock.acquire()
    return str(True)
@app.route('/givePrio')
def releasePriority():
    try :
        lock.release()
        return str(True)
    except RuntimeError :
        return "Release quelque chose de déjà release"


# --------------------------------------
#   Initialisation de début de game
# --------------------------------------