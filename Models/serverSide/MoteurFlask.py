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
        self._units =[]
        # Marines
        m= cg.Marines
        self._units.append("4:"+str(m[0])+","+str(m[1])+","+str(m[2])+","+str(m[3])+",Marines")
        m = cg.Artilleur
        self._units.append("4:"+str(m[0])+","+str(m[1])+","+str(m[2])+","+str(m[3])+",Artilleur")
        m = cg.Eclaireur
        self._units.append("4:"+str(m[0])+","+str(m[1])+","+str(m[2])+","+str(m[3])+",Eclaireur")

       # self._units = ["4:2,5,4,2,Marines","4:1,2,3,3,Artilleur","2:4,1,0,5,Eclaireur"]

        self.land = Land(self._tailleTerrain)
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
        team = Team(teamName, self._positionPossibleBase[self._currentPosition])
        self._currentPosition += 1
        self._equipe[teamName] = team
        return team.basePosition

    # En fonction de la team, en bas a hauche ou en haut a droite
    def getPositionDrapeau(self, teamName):
        return self._equipe[teamName].basePosition


    # Renvoi les unités disponibles pour la partie
    def getStartUnite(self):
        return self._units

    # Enregistre l'unité selon un certain type, un certain nom, à un position
    def registerUnite(self, team, unitType, unitName, posX, posY):

        return self._equipe[team].registerUnit(unitType,unitName,posX, posY)

    # -------------------------------------------------------------------
    # ----------------- CONCERNANT LE FONCTIONNEMENT --------------------
    # -------------------------------------------------------------------

    def deplacementUnite(self, name, position):
        pass

    def shoot(self, name, position):
        pass

