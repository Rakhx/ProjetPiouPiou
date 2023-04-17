import random

from ProjectPiouPiou.Models.bo.Base import Base
from ProjectPiouPiou.Models.bo.Flag import Flag
from ProjectPiouPiou.Models.bo.Land import Land
from ProjectPiouPiou.Models.bo.Obstacle import Obstacle
from ProjectPiouPiou.Models.serverSide.Team import Team
from ProjectPiouPiou.Presenter.PresenterConsole import PresenterConsole
from ProjectPiouPiou.View.ConsoleView import ConsoleView
import ProjectPiouPiou.Models.bo.config as cg
import traceback


class MoteurFlask():

    def __init__(self):
        self._view = ConsoleView()
        self._presenter = PresenterConsole(self._view)

        self._tailleTerrain = cg.tailleTerrainTuple
        self._unitsTypeAvailable =[]

        m= cg.Marines
        self._unitsTypeAvailable.append("4:" + str(m[0]) + "," + str(m[1]) + "," + str(m[2]) + "," + str(m[3]) + ",Marines")
        m = cg.Artilleur
        self._unitsTypeAvailable.append("4:" + str(m[0]) + "," + str(m[1]) + "," + str(m[2]) + "," + str(m[3]) + ",Artilleur")
        m = cg.Eclaireur
        self._unitsTypeAvailable.append("2:" + str(m[0]) + "," + str(m[1]) + "," + str(m[2]) + "," + str(m[3]) + ",Eclaireur")
        # self._units = ["4:2,5,4,2,Marines","4:1,2,3,3,Artilleur","2:4,1,0,5,Eclaireur"]

        self._land = Land(self._tailleTerrain)
        self._equipe = {}
        self._currentIndex = 0
        # TODO A randomiser
        self._positionPossibleBase = [(1, 1), (self._tailleTerrain[0] - 1, self._tailleTerrain[1] - 1),
                                      (1, self._tailleTerrain[1] - 1), (self._tailleTerrain[1] - 1, 1)]

        self._land.generateObstacle(0.05)
        # clear obstacle include dans la fn
        self._land.generateFlag()
        for pos in self._positionPossibleBase:
            self._land.clearObstacleAroundPosition(pos)

        # Concernant la boucle de jeu
        # Liste des unites ayant déjà pendant ce tour tiré, bougé, etc
        self._alrdyMov = []
        self._alrdyShoot = []
        self._alrdyLooked = []

    # ---------------------
    # Fonction interne a la classe
    # ---------------------

   # # TODO A randomiser
   #  def generateFlag(self):
   #      pos = (self._tailleTerrain[0]//2, self._tailleTerrain[1]//2)
   #      self._land.clearObstacleAroundPosition(pos)
   #      flag = Flag("Flag","Neutre", pos, 0, 0, 0, False)
   #      self._land.addItem(flag)

    # # genere les obstacles sur la map, aléatoirement
    # def generateObstacle(self, pourcentage):
    #     maxX = self._land.getDimension[0]
    #     maxY = self._land.getDimension[1]
    #     nbCase = maxX * maxY
    #     nbObstacle = int(nbCase * pourcentage)
    #     for i in range(nbObstacle) :
    #         x = random.uniform(0, maxX)
    #         y = random.uniform(0, maxY)
    #         # si la case est pas déjà prise
    #         if not (x,y) in self._land.getPlateau() :
    #             obs = Obstacle((x,y))
    #             self._land.getPlateau()[(x,y)] = obs
    #             self._land.getPlateau().append(obs)
    #
    # # Etabli un périmètre autour d'une case pour clean. ( drapeau et départ de team )
    # def clearObstacleAroundPosition(self, position):
    #     for x in range(-1, 2):
    #         for y in range(-1, 2):
    #             pos = (position[0]+x, position[1]+y)
    #             if pos in self._land.getPlateau() :
    #                 itemToRmv = self._land.getPlateau().pop(pos)
    #                 self._land.removeItem(itemToRmv)




    # -------------------------------------------------------------------
    # ------------------ CONCERNANT L'INITIALISATION --------------------
    # -------------------------------------------------------------------
    def getTailleMap(self):
        return self._tailleTerrain

    # Prendre le nom des équipes, renvoi la position de l'équipe
    def registerTeam(self, teamName):
        numeroTeam = self._currentIndex
        positionTeam = self._positionPossibleBase[self._currentIndex]
        # self._equipeFromNumToName[numeroTeam] = teamName
        team = Team(teamName, numeroTeam, positionTeam, self._land)
        base = Base(positionTeam, teamName)
        self._land.addItem(base)
        self._land.clearObstacleAroundPosition(positionTeam)
        self._equipe[teamName] = team
        self._currentIndex += 1
        cg.equipes[teamName] = numeroTeam
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
        self._alrdyMov = []
        self._alrdyShoot = []
        self._alrdyLooked = []

        resultat = self._land.getResume(teamName)
        return resultat

    def displayLand(self):
        return self._presenter.parseLand(self._land)

    # Une unité regarde autour d'elle
    # retour k:position v: unitTYpe
    def regardeAutour(self, teamName, unitName):
        try :
            team = self._equipe[teamName]
            unite = team.getUnitByName(unitName)
        except :
            if cg.debug:
                print("[MoteurFlask.regardeAutour({})] Clef n'existe pas".format(unitName))
            return "[MoteurFlask.regardeAutour({})] Clef n'existe pas".format(unitName)

        if unite in self._alrdyLooked:
            return "ALRDY_LOOK"
        self._alrdyLooked.append(unite)

        retour = self._land.lookAround(unite.getPosition(), unite.getVision())
        if cg.debug:
            print(retour)

        return retour

    # Retour
    # NO_CASE : case déjà prise
    # NO_REACH : l'unité n'a pas la portée
    # NO_PASS : Pas de chemin disponible
    # ALRDY_MOVE : l'unité s'est déjà déplacée ce tour ci
    def deplacementUnite(self, teamName, unitName, position):

        try :
            team = self._equipe[teamName]
            unite = team.getUnitByName(unitName)

            # On vérifie que l'unité ne s'est pas encore déplacée à ce tour
            if unite in self._alrdyMov:
                return "ALRDY_MOV"
            self._alrdyMov.append(unite)

            # Verification que la case est disponible
            if self._land.getItemOrFalseAtPosition(position):
                return "NO_CASE"

            # Verification que l'unité peut atteindre la case
            posUnit = unite.getPosition()
            # on regarde toutes les cases qui pourraient faire l'affaire autour de posUnit
            casesMaybe = self._land.getCasesAtRange(posUnit, unite.getMvt())
            # On vérifie récursivement quelles sont les cases accessibles
            posNearFine = []
            self._land.exploRecu(posNearFine, casesMaybe, posUnit, unite.getMvt())

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

        self._land.moveItem(unite, position)
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

            # On vérifie que l'unité n'a pas encore tiré
            if unite in self._alrdyShoot:
                return "ALRDY_SHOOT"
            self._alrdyShoot.append(unite)

            # on vérifie que l'unité a la portée pour tirer
            casesMaybe = self._land.getCasesAtRange(posUnit, unite.getVision())
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

            if cg.debug:
                print("unite ", unite.getName(), " a tiré sur ", cible.getName(), "il lui reste ",
                      pvRestant)

        except KeyError:
            print("[MoteurFlask.deplacementUnite({})] no such unit".format(unitName))
            return "[MoteurFlask.deplacementUnite({})] no such unit".format(unitName)
        except Exception as e:
            print(traceback.format_exc())
            print("[MoteurFlask.deplacementUnite()] autre erreur: ", repr(e))
            return "[MoteurFlask.deplacementUnite()] autre erreur " + repr(e)

        self._land.moveItem(unite, position)
        return "OK"

