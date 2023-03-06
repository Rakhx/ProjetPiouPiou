from ProjectPiouPiou.Models.bo.Land import Land
from ProjectPiouPiou.Models.serverSide.Team import Team
from ProjectPiouPiou.Presenter.PresenterConsole import PresenterConsole
from ProjectPiouPiou.View.ConsoleView import ConsoleView
import ProjectPiouPiou.Models.bo.config as cg


#
class MoteurFlask():

    def __init__(self):
        view = ConsoleView()
        presenter = PresenterConsole(view)

        self._tailleTerrain = cg.tailleTerrainTuple
        self._unitsTxt =[]
        # Marines
        m= cg.Marines
        self._unitsTxt.append("4:" + str(m[0]) + "," + str(m[1]) + "," + str(m[2]) + "," + str(m[3]) + ",Marines")
        m = cg.Artilleur
        self._unitsTxt.append("4:" + str(m[0]) + "," + str(m[1]) + "," + str(m[2]) + "," + str(m[3]) + ",Artilleur")
        m = cg.Eclaireur
        self._unitsTxt.append("4:" + str(m[0]) + "," + str(m[1]) + "," + str(m[2]) + "," + str(m[3]) + ",Eclaireur")

       # self._units = ["4:2,5,4,2,Marines","4:1,2,3,3,Artilleur","2:4,1,0,5,Eclaireur"]

        self._land = Land(self._tailleTerrain)
        self._equipe = {}
        self._positionPossibleBase = [(1, 1), (self._tailleTerrain[0] - 1, self._tailleTerrain[1] - 1),
                                      (1, self._tailleTerrain[1] - 1), (self._tailleTerrain[1] - 1, 1)]
        self._currentPosition = 0

    # ---------------------
    # Fonction interne a la classe
    # ---------------------
    def __generateFlag(self):
        pass

    # -------------------------------------------------------------------
    # ------------------ CONCERNANT L'INITIALISATION --------------------
    # -------------------------------------------------------------------
    def getTailleMap(self):
        return self._tailleTerrain

    # Prendre le nom des équipes, renvoi la position de l'équipe
    def registerTeam(self, teamName):
        team = Team(teamName, self._positionPossibleBase[self._currentPosition], self._land)
        self._currentPosition += 1
        self._equipe[teamName] = team
        return team.basePosition

    # En fonction de la team, en bas a hauche ou en haut a droite
    def getPositionDrapeau(self, teamName):
        return self._equipe[teamName].basePosition

    # Renvoi les unités disponibles pour la partie
    def getStartUnite(self):
        return self._unitsTxt

    # Enregistre l'unité selon un certain type, un certain nom, à un position
    def registerUnite(self, team, unitType, unitName, posX, posY):
        return self._equipe[team].registerUnit(unitType,unitName,posX, posY)

    # -------------------------------------------------------------------
    # ----------------- CONCERNANT LE FONCTIONNEMENT --------------------
    # -------------------------------------------------------------------


    # TODO
    # Une unité regarde autour d'elle
    def regardeAutour(self, teamName, unitName):
        try :
            team = self._equipe[teamName]
            unite = team.getUnitByName(unitName)
        except :
            if cg.debug.debug:
                print("[MoteurFlask.regardeAutour({}) Clef n'existe pas".format(unitName))
            return "[MoteurFlask.regardeAutour({}) Clef n'existe pas".format(unitName)

        print("jj",self._land.lookAround(unite.getPosition(), unite.getRange()))
        return self._land.lookAround(unite.getPosition(), unite.getRange())

    # Retour
    # NO_CASE : case déjà prise
    # NO_REACH : l'unité n'a pas la portée
    # NO_PASS : Pas de chemin disponible
    def deplacementUnite(self, teamName, unitName, position):

        try :

            team = self._equipe[teamName]
            unite = team.getUnitByName(unitName)
            # Verification que l'unité peut atteindre la case
            posUnit = self._unitsTxt[unitName].getPosition()


            # Verification que la case est disponible
            if not self._land.getItemOrTrueAtPosition(position):
                return "NO_CASE"
        except :
            print("[MoteurFlask.deplacementUnite({}) no such unit".format(unitName))
            return "[MoteurFlask.deplacementUnite({}) no such unit".format(unitName)


        pass

    # TODO
    # Tire sur la case selectionnée, dommage fait si cible
    def shoot(self, name, position):
        pass

