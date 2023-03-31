
class Automaton:
    def __init__(self, serveur):
        self._server = serveur
        self._name = "derrGolem"
        self._server.registerTeam(self._name)
        self._startPosition = (39,39)
        self._tailleTerrain = (40,40)
        self.registerUnits()


    # Déploie 4 unités autour de la abse
    def registerUnits(self):
        param = {"team": self._name, "type": "Eclaireur", "name": "botEcl1", "posX": self._startPosition[0] - 1,
                 "posY": self._startPosition[1] - 1}
        self._server.registerUnit(param)
        param = {"team": self._name, "type": "Eclaireur", "name": "botEcl2", "posX": self._startPosition[0] + 1,
                 "posY": self._startPosition[1] + 1}
        self._server.registerUnit(param)
        param = {"team": self._name, "type": "Marines", "name": "botMar", "posX": self._startPosition[0] + 1,
                 "posY": self._startPosition[1] - 1}
        self._server.registerUnit(param)
        param = {"team": self._name, "type": "Artilleur", "name": "botArt", "posX": self._startPosition[0] - 1,
                 "posY": self._startPosition[1] + 1}
        self._server.registerUnit(param)


    def playTurn(self):
        # pour le moment, do NOTHING
        pass

