import time
from threading import Lock
from flask import Flask, request
from ProjectPiouPiou.Models.serverSide.MoteurFlask import MoteurFlask
import ProjectPiouPiou.Models.bo.config as cg
import tkinter as tk
from tkinter import *

from threading import Thread



def display_land(var):
    ROOT = Tk()
    LABEL = Label(ROOT, text="Hello, world!")
    LABEL.pack()

    while True:
        time.sleep(2)
        with data_lock:
            label = Label(ROOT, text=var[0])
        label.pack()
        ROOT.update()


data_lock = Lock()

# --------------------------------------
#   Element autre de la classe
# --------------------------------------
app = Flask(__name__)
moteur = MoteurFlask()
lock = Lock()
teamWithPrio = ""
tempValue = ["hihi"]
T = Thread(target=display_land, args=(tempValue,))
print("hum?")
T.start()


def modifyValue():
    with data_lock:
        global tempValue
        tempValue[0] = tempValue[0] + "hi"

def seeValue():
    with data_lock:


        print(tempValue)

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
    message = moteur.registerUnite(test["team"],test["type"],test["name"],test["posX"], test["posY"])
    if cg.debug :
        print("Register unit ", test["name"], "de type: " , test["type"], " pour team", test["team"],
                " position ",test["posX"],"x",test["posY"] , ":" ,message)

    return message

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

# --------------------------------------
#   Boucle en cours de  game
# --------------------------------------

# regarde autour
@app.route('/loop/lookAround', methods=['GET'])
def regarderAutour():
    param =  request.args.to_dict()
    modifyValue()
    seeValue()
    return [tuple(str(x) for x in moteur.regardeAutour(param["team"],param["unitName"]))]


@app.route('/loop/move', methods=['GET'])
def deplacementUnite():
    param =  request.args.to_dict()
    return moteur.deplacementUnite(param["team"],param["unitName"], (int(param["posX"]), int(param["posY"])))

@app.route('/loop/shoot', methods=['GET'])
def tirer():
    param = request.args.to_dict()
    return moteur.shoot(param["team"], param["unitName"], (int(param["posX"]), int(param["posY"])))

# --------------------------------------
# Mutex stuff
# --------------------------------------
@app.route('/loop/askPrio', methods=['GET'])
def getPriority():
    param = request.args.to_dict()
    lock.acquire()
    teamWithPrio = param["team"]
    if cg.debug :
        print("equipe " + param["team"] + " prend la priorite")

    moteur.displayLand()
    return moteur.sumupSituation(param["team"])

@app.route('/loop/releasePrio')
def releasePriority():
    try :
        lock.release()
        if cg.debug:
            print("equipe ", teamWithPrio," release la priorite")
        return str(True)
    except RuntimeError :
        return "Release quelque chose de déjà release"

