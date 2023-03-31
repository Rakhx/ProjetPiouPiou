import json
import time
import requests

from ProjectPiouPiou.FakeClient.Automaton import Automaton
from ProjectPiouPiou.FakeClient.MockServer import MockServer


# Classe qui va permettre de faire communiquer votre code avec le serveur.
class MockClient():

    def __init__(self, teamName):
        self._server = MockServer()
        self._name = teamName
        self._server.registerTeam(teamName)
        # Position de départ
        self.startPosition = (1,1)
        # Taille du terrain
        self.tailleLand = (40,40)
        self.unitDispos = ["4:2,5,4,2,Marines","4:1,2,3,3,Artilleur","2:4,1,0,5,Eclaireur"]
        # AJout du bot
        self._automate = Automaton(self._server)


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
        param = {}
        param["team"] = self._name
        param["type"] = unitType
        param["name"] = unitName
        param["posX"] = pos[0]
        param["posY"] = pos[1]
        return self._server.registerUnit(param)


    # --------------------------------------
    #   Boucle en cours de  game
    # --------------------------------------

    # fonction a appeler dans le while
    def newTurn(self):
        time.sleep(.1)
        # fait jouer le bot
        self._automate.playTurn()

        # renvoyer son propre terrain si on veut tester correctement
        boardState = []
        return boardState

    def regarderAutour(self, unitName):
        param = {}
        param["team"] = self._name
        param["name"] = unitName
        return self._server.regarderAutour(param)

    def deplacer(self, unitName, pos):
        param = {}
        param["team"] = self._name
        param["unitName"] = unitName
        param["posX"] = pos[0]
        param["posY"] = pos[1]
        return self._server.deplacementUnite(param)

    def tirer(self, unitName, pos):
        param = {"team": self._name, "name": unitName, "posX": pos[0], "posY": pos[1]}
        return self._server.tirer(param)


    # Fait jouer le bot
    def newTurn(self):
        time.sleep(1)
        boardState = self._server.sumUpSituaiton({"team" : self._name})
        return (boardState)


    # --------------------------------------
    #   Autres
    # --------------------------------------
    def posString(self, pos):
        return "&posX=" + str(pos[0])+ "&posY=" + str(pos[1])


