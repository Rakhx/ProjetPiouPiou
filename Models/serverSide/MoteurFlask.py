from ProjectPiouPiou.Models.bo.Land import Land
from ProjectPiouPiou.Models.serverSide.Team import Team
from ProjectPiouPiou.Presenter.PresenterConsole import PresenterConsole
from ProjectPiouPiou.View.ConsoleView import ConsoleView
import ProjectPiouPiou.Models.bo.config as cg
import traceback


#
class MoteurFlask():

    def __init__(self):
        self._view = ConsoleView()
        self._presenter = PresenterConsole(self._view)

        self._tailleTerrain = cg.tailleTerrainTuple
        self._unitsTypeAvailable =[]
        # Marines
        m= cg.Marines
        self._unitsTypeAvailable.append("4:" + str(m[0]) + "," + str(m[1]) + "," + str(m[2]) + "," + str(m[3]) + ",Marines")
        m = cg.Artilleur
        self._unitsTypeAvailable.append("4:" + str(m[0]) + "," + str(m[1]) + "," + str(m[2]) + "," + str(m[3]) + ",Artilleur")
        m = cg.Eclaireur
        self._unitsTypeAvailable.append("2:" + str(m[0]) + "," + str(m[1]) + "," + str(m[2]) + "," + str(m[3]) + ",Eclaireur")

       # self._units = ["4:2,5,4,2,Marines","4:1,2,3,3,Artilleur","2:4,1,0,5,Eclaireur"]

        self._land = Land(self._tailleTerrain)
        self._equipe = {}
        self._positionPossibleBase = [(1, 1), (self._tailleTerrain[0] - 1, self._tailleTerrain[1] - 1),
                                      (1, self._tailleTerrain[1] - 1), (self._tailleTerrain[1] - 1, 1)]
        self._currentPosition = 0

    # ---------------------
    # Fonction interne a la classe
    # ---------------------

   # TODO
    def __generateFlag(self):
        pos = ()

        self._land.clearObstacleAroundPosition(pos)

        pass

    # -------------------------------------------------------------------
    # ------------------ CONCERNANT L'INITIALISATION --------------------
    # -------------------------------------------------------------------
    def getTailleMap(self):
        return self._tailleTerrain

    # Prendre le nom des équipes, renvoi la position de l'équipe
    def registerTeam(self, teamName):
        team = Team(teamName, self._positionPossibleBase[self._currentPosition], self._land)
        self._land.clearObstacleAroundPosition(self._positionPossibleBase[self._currentPosition])
        self._currentPosition += 1
        self._equipe[teamName] = team
        return team.basePosition

    # En fonction de la team, en bas a hauche ou en haut a droite
    def getPositionDrapeau(self, teamName):
        return self._equipe[teamName].basePosition

    # Renvoi les unités disponibles pour la partie
    def getStartUnite(self):
        return self._unitsTypeAvailable

    # Enregistre l'unité selon un certain type, un certain nom, à un position
    def registerUnite(self, team, unitType, unitName, posX, posY):
        return self._equipe[team].registerUnit(unitType,unitName,posX, posY)

    # -------------------------------------------------------------------
    # ----------------- CONCERNANT LE FONCTIONNEMENT --------------------
    # -------------------------------------------------------------------

    # Fait un résumé des unités disponibles sur la map pour une équipe, pv restant et position. Le
    # retour est sous la forme key: unite v : (position, pv), position étant (x,y)
    def sumupSituation(self, teamName):
        resultat = self._land.getResume(teamName)
        return resultat

    def displayLand(self):
        self._presenter.parseLand(self._land)

    # Une unité regarde autour d'elle
    def regardeAutour(self, teamName, unitName):
        try :
            team = self._equipe[teamName]
            unite = team.getUnitByName(unitName)
        except :
            if cg.debug.debug:
                print("[MoteurFlask.regardeAutour({}) Clef n'existe pas".format(unitName))
            return "[MoteurFlask.regardeAutour({}) Clef n'existe pas".format(unitName)

        print(self._land.lookAround(unite.getPosition(), unite.getRange()))
        self.displayLand()
        return self._land.lookAround(unite.getPosition(), unite.getRange())

    # Retour
    # NO_CASE : case déjà prise
    # NO_REACH : l'unité n'a pas la portée
    # NO_PASS : Pas de chemin disponible
    def deplacementUnite(self, teamName, unitName, position):

        try :
            team = self._equipe[teamName]
            unite = team.getUnitByName(unitName)

            # Verification que la case est disponible
            if self._land.getItemOrFalseAtPosition(position):
                return "NO_CASE"

            # Verification que l'unité peut atteindre la case
            posUnit = unite.getPosition()
            # on regarde toutes les cases qui pourraient faire l'affaire autour de posUnit
            casesMaybe = self._land.getCasesAtRange(posUnit, unite.getRange())
            # On vérifie récursivement quelles sont les cases accessibles
            posNearFine = []
            self._land.exploRecu(posNearFine, casesMaybe,posUnit, unite.getRange())

            # on enleve de ces cases celles qui contiennent des unités alliées ou ennemies
            posOk = self._land.cleanCase(posNearFine)

            # On renvoie un message d'erreur adaptée
            if(position not in posNearFine):
                return "NO_REACH"

            if(position not in posOk):
                return "NO_PASS"

        except KeyError:
            print("[MoteurFlask.deplacementUnite({})] no such unit".format(unitName))
            return "[MoteurFlask.deplacementUnite({})] no such unit".format(unitName)
        except Exception as e :
            print(traceback.format_exc())
            print("[MoteurFlask.deplacementUnite()] autre erreur: ", repr(e))
            return "[MoteurFlask.deplacementUnite()] autre erreur " + repr(e)

        self._land.moveItem( unite, position )
        self._presenter.parseLand(self._land)

        return "OK"

    # Tire sur la case selectionnée, dommage fait si cible
    # NO_REACH : pas la portée
    # OUT_SIGHT : tir ok mais pas de réponse
    # OK_NOKILL : touché mais pas tué
    # OK_KILL : touché et éliminé
    # KO_INTERCEPT : touché objet avant la cible
    def shoot(self, teamName, unitName, position):

        try :
            team = self._equipe[teamName]
            unite = team.getUnitByName(unitName)
            posUnit = unite.getPosition()

            # on vérifie que l'unité a la portée pour tirer
            casesMaybe = self._land.getCasesAtRange(posUnit, unite.getRange())
            if not position in casesMaybe :
                return "NO_REACH"

            # On vérifie si un obstacle ou une unite ennemi se trouve sur le chemin
            # TODO

            # on récupère l'item positionné à l'emplacement, s'il existe
            if not position in self._land._plateau :
                return "KO_NOTOUCH"

            cible = self._land._plateau.get(position)
            degat = unite.getDegat()
            pvRestant = cible.takeShoot(degat)

            if( cg.debug):
                print("unite ", unite.getName(), " a tiré sur ", cible.getName(), "il lui reste ",
                      pvRestant)


        except KeyError:
            print("[MoteurFlask.deplacementUnite({})] no such unit".format(unitName))
            return "[MoteurFlask.deplacementUnite({})] no such unit".format(unitName)
        except Exception as e :
            print(traceback.format_exc())
            print("[MoteurFlask.deplacementUnite()] autre erreur: ", repr(e))
            return "[MoteurFlask.deplacementUnite()] autre erreur " + repr(e)

        self._land.moveItem( unite, position )
        self._presenter.parseLand(self._land)

        return "OK"

