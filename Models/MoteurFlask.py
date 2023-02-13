from ProjectPiouPiou.Models.bo.Land import Land
from ProjectPiouPiou.Models.serverSide.Team import Team
from ProjectPiouPiou.Presenter.PresenterConsole import PresenterConsole
from ProjectPiouPiou.View.ConsoleView import ConsoleView


#
class MoteurFlask():

    def __init__(self):
        view = ConsoleView()
        presenter = PresenterConsole(view)
        self.tailleTerrain = (50,50)
        self.land = Land(self.tailleTerrain)
        self._equipe = {}
        self._positionFlag = [(1,1), (self.tailleTerrain[0]-1, self.tailleTerrain[1]-1)]
        self._currentPosition = 0

    # ---------------------
    # Concernant les get initiaux
    # ---------------------
    def getTailleMap(self):
        return self.tailleTerrain

    # Prendre le nom des équipes
    def registerTeam(self, name):
        team = Team(name, self._positionFlag[self._currentPosition])
        self._currentPosition += 1
        self._equipe[name] = team

    # En fonction de la team, en bas a hauche ou en haut a droite
    def getPositionDrapeau(self, name):
        return self._equipe[name].flag


    # pour l'instant, renvoi les 1 marines et un artilleur
    def getStartUnite(self):
        return "1 : 2,5,4,2, marines \n 1 : 1,2,3,3, artilleur"

    #
    def registerUnite(self, team ,unitName, unitType, position):


        # Verification de la disponibilité des cases
        pass

    # ---------------------
    # AU fur et a mesure
    # ---------------------

    def deplacementUnite(self, name, position):
        pass

    def shoot(self, name, position):
        pass

