import json
import time
import requests

# Classe qui va permettre de faire communiquer votre code avec le serveur.
class MockClient():

    def __init__(self, teamName):
        self._name = teamName
        # Position de départ

        self._startPosition = (1,1)
        # Taille du terrain

        self._tailleLand = (40,40)

        self._unitDispos = ["4:2,5,4,2,Marines","4:1,2,3,3,Artilleur","2:4,1,0,5,Eclaireur"]

    # --------------------------------------
    #   Initialisation de début de game
    # --------------------------------------


    # Enregistre une unité sur le serveur. Le serveur renvoi un message
    # OK = unité positionnée
    # ERR_EXIST = unité selectionnée n'existe pas ( faute de frappe? )
    # ERR_DISPO = unité selectionnée pas disponible
    # ERR_NAME = nom de l'unité déjà utilisé
    # ERR_PLACE = Positionnement de l'unité non disponible
    def registerUnit(self, unitType,unitName, pos):
        return "OK"



    # --------------------------------------
    #   Boucle en cours de  game
    # --------------------------------------

    # fonction a appeler dans le while
    def newTurn(self):
        time.sleep(1)
        # renvoyer son propre terrain si on veut tester correctement
        boardState = []
        return boardState


    def regarderAutour(self, unitName):
        r = requests.get("http://127.0.0.1:5000/loop/lookAround?team="+self._name + "&unitName=" + unitName)
        received = json.loads(r.text)
        return tuple(i for i in received)

    def deplacer(self, unitName, pos):
        r = requests.get("http://127.0.0.1:5000/loop/move?team="+self._name + "&unitName=" + unitName + self.posString(pos))
        return r.text

    def tirer(self, unitName, pos):
        r = requests.get("http://127.0.0.1:5000/loop/shoot?team=" + self._name + "&unitName=" + unitName + self.posString(pos))
        return r.text

    # --------------------------------------
    #   Autres
    # --------------------------------------
    def posString(self, pos):
        return "&posX=" + str(pos[0])+ "&posY=" + str(pos[1])

