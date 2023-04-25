import ProjectPiouPiou.Models.bo.config as cg
from ProjectPiouPiou.Models.bo.Artilleur import Artilleur
from ProjectPiouPiou.Models.bo.Eclaireur import Eclaireur
from ProjectPiouPiou.Models.bo.Marines import Marines
from ProjectPiouPiou.Models.bo.Obstacle import Obstacle

class Automaton:
    def __init__(self, serveur):
        self._server = serveur
        self._name = "derrGolem"
        self._server.registerTeam(self._name)
        self._tailleTerrain = cg.tailleTerrainTuple
        self._startPosition = (cg.tailleTerrainTuple[0]-1, cg.tailleTerrainTuple[1]-1)
        self._uniteDispo = serveur.getUniteDispos()
        self._mesUnites = []
        self.registerUnits()
        self._posMechants = []
        self._mapCenter = (cg.tailleTerrainTuple[0]//2, cg.tailleTerrainTuple[1]//2)

    # Déploie 4 unités autour de la abse
    def registerUnits(self):
        posX = self._startPosition[0]
        posY = self._startPosition[1]

        stats = self._uniteDispo[0].split(':')[1].split(',')
        param = {"team": self._name, "type": "Marines", "name": "botMar", "posX": self._startPosition[0] + 1,
                 "posY": self._startPosition[1] + 1}
        self._server.registerUnit(param)
        mar1 = Marines("botMar", self._name, (posX + 1, posY + 1), stats[0], stats[1], stats[2], stats[3])
        self._mesUnites.append(mar1)

        stats = self._uniteDispo[1].split(':')[1].split(',')
        param = {"team": self._name, "type": "Artilleur", "name": "botArt", "posX": self._startPosition[0] - 1,
                 "posY": self._startPosition[1] - 1}
        self._server.registerUnit(param)
        art1 = Artilleur("botArt", self._name, (posX - 1, posY - 1), stats[0], stats[1], stats[2], stats[3])
        self._mesUnites.append(art1)

        stats = self._uniteDispo[2].split(':')[1].split(',')
        param = {"team": self._name, "type": "Eclaireur", "name": "botEcl1", "posX": self._startPosition[0] - 1,
                 "posY": self._startPosition[1] + 1}
        self._server.registerUnit(param)
        eclai1 = Eclaireur("botEcl1", self._name, (posX - 1, posY + 1), stats[0], stats[1], stats[2], stats[3])
        self._mesUnites.append(eclai1)

        param = {"team": self._name, "type": "Eclaireur", "name": "botEcl2", "posX": self._startPosition[0] + 1,
                 "posY": self._startPosition[1] - 1}
        self._server.registerUnit(param)
        eclai2 = Eclaireur("botEcl2", "létrofor", (posX + 1, posY - 1), stats[0], stats[1], stats[2], stats[3])
        self._mesUnites.append(eclai2)

    def playTurn(self):
        self._posMechants.clear()
        param = {"team": self._name}

        # Regarder autour
        for unite in self._mesUnites :
            param["unitName"] = unite.getName()
            vu = self._server.regarderAutour(param)
            dic = cg.fromListTodic(vu)

            for key in dic :
                if dic[key] != "O":
                    if not key in self._posMechants:
                      self._posMechants.append(key)

        # Deplacement des unités
        if not self._posMechants:
            target = self._mapCenter
        else :
            target = self._posMechants[0]

        for unite in self._mesUnites:
            posVoulu = unite.moveRandomlyToward(target)
            param["unitName"] = unite.getName()
            param["posX"] = posVoulu[0]
            param["posY"] = posVoulu[1]
            resultat = self._server.deplacementUnite(param)
            if(resultat == "OK"):
                unite.setPosition(posVoulu)

        # Tire des unites
        tirOk = True
        for unite in self._mesUnites:
            if target == unite.getPosition():
                tirOk = False

        if tirOk :
            param["posX"] = target[0]
            param["posY"] = target[1]
            for unite in self._mesUnites:
                param["unitName"] = unite.getName()
                self._server.tirer(param)


