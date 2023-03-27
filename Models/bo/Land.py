# Classe qui correspond au terrain sur lequel se déroule la partie
import math
import random
from typing import Tuple
from typing import List

from ProjectPiouPiou.Models.bo.Flag import Flag
from ProjectPiouPiou.Models.bo.Item import Item
from ProjectPiouPiou.Models.bo.Obstacle import Obstacle

class Land():
    def __init__(self, dimension : Tuple[float, float] = (), items : List[Item] = [] ):
        # Tuple de hauteur par largeur
        self._dimension = dimension
        # Liste des items contenu sur la map
        self._items = items
        # dictionnaire k:position v:item
        self._plateau = {}
        for itemz in items:
            self._plateau[itemz.getPosition()] = itemz

    def getDimension(self) -> Tuple[float, float]:
        return self._dimension
    def getPlateau(self):
        return self._plateau
    def addItem(self, item : Item ):
        self._items.append(item)
        self._plateau[item.getPosition()] = item

    def removeItem(self, item : Item):
        self._plateau.pop(item.getPosition())
        self._items.remove(item)

    def getItems(self):
        return self._items

    def getResume(self, teamName):
        resume = []
        for pos in self._plateau:
            item = self._plateau[pos]
            if(item.getTeamName() == teamName):
                resume.append( (pos,item.getName(), item.getPosition()[0], item.getPosition()[1], item.getPV()))
        print(resume)
        return resume

    def moveItem(self, item, position):
        self._plateau[position] = item
        del self._plateau[item.getPosition()]
        item.setPosition(position)

    # Renvoi l'objet a la position donnée, ou False si case disponible
    def getItemOrFalseAtPosition(self, position : Tuple[float, float]):
        if position in self._plateau:
            return self._plateau[position]
        return False

    # Renvoi les cases accessibles depuis la position en paramètre
    def getCasesAtRange(self, position, portee):
        positionBarelyAtRange = []
        positionAtRange = []

        # Commence par un découpage grossier
        for x in range(-portee, portee + 1) :
            for y in range(-portee, portee + 1):
                pos = (position[0]+x, position[1]+y)
                if(pos[0] >= 0 and pos[1] >= 0):
                    positionBarelyAtRange.append( pos )
        # puis vérifie que chaque case est a portée de cercle
        for positionLooked in positionBarelyAtRange:
            if self.isAtCircleRange(position, positionLooked, portee):
                positionAtRange.append(positionLooked)

        return positionAtRange

    # Vérifie que le centre de la case d'arrivée est dans le cercle depuis la position de départ
    def isAtCircleRange(self, posDepart, posArrivee, range):
        centreDepart = posDepart + (0.5, 0.5)
        centreArrivee = posArrivee + (0.5, 0.5)
        # si la distance entre les deux centres est inférieur au rayon
        distance = math.sqrt( math.pow(centreDepart[0]-centreArrivee[0],2) + math.pow(centreDepart[1]-centreArrivee[1],2) )
        return distance <= range

    # Une unité regarde autour d'elle
    def lookAround(self, position, portee):
        retour = {}
        team = self._plateau[position].getTeamName()
        for x in range(-1,portee+1):
            for y in range(-1,portee+1):
                if x != 0 or y != 0:
                    pos = (int(position[0])+int(x), int(position[1])+int(y))
                    # Si case a portée, et contenant un item
                    if self.isAtCircleRange(position, pos, portee) and pos in self._plateau:
                        # si l'item ne fait pas parti de la meme team
                        if not self._plateau[pos] == team :
                            retour[pos] = self._plateau[pos].getShortRepresentation()

        return retour

    # inverse le contenu du plateau pour pos1 et pos2
    def deplacerUnite(self, position1, position2):

        pass

    # retourne les positions directement connexe a la position. Croix sans diagonale.
    def getPosConnexe(self, position):
        retour = []
        retour.append((position[0]+ 1, position[1]))
        retour.append((position[0]- 1, position[1]))
        retour.append((position[0], position[1]+ 1 ))
        retour.append((position[0], position[1]- 1 ))
        return retour

    # fonction récursive pour trouver les cases accessibles, en prennant en compte les obstacles
    def exploRecu(self, posOk, posPossible, currentPos,  range):
        range -= 1
        # for each case autour, on va voir si on continu a explorer à partir de cette case
        for position in self.getPosConnexe(currentPos):
            # On vérifie qu'il n'y a pas d'obstacle sur la case
            if (position not in self._plateau) or (not isinstance(self._plateau[position],Obstacle)) :
                # si la case est encore dans la liste des casePossible, et n'a pas été checké
                if(position in posPossible and position not in posOk):
                    posOk.append(position)
                    posPossible.remove(position)

                if(range > 0):
                    self.exploRecu(posOk, posPossible, position, range)


    # retourne une liste qui contient toutes les cases vides
    def cleanCase(self, listCase):
        caseClean = []
        for pos in listCase:
            if not pos in self._plateau:
                caseClean.append(pos)
        return caseClean

    # genere les obstacles sur la map, aléatoirement
    def generateObstacle(self, pourcentage):
        maxX = self._dimension[0]
        maxY = self._dimension[1]
        nbCase = maxX * maxY
        nbObstacle = int(nbCase * pourcentage)
        for i in range(nbObstacle) :
            x = random.uniform(0, maxX)
            y = random.uniform(0, maxY)
            # si la case est pas déjà prise
            if not (x,y) in self._plateau :
                obs = Obstacle((x,y))
                self._plateau[(x,y)] = obs
                self._items.append(obs)

    def generateFlag(self):
        pos = (self._dimension[0]//2, self._dimension[1]//2)
        self.clearObstacleAroundPosition(pos)
        flag = Flag("Flag","Neutre", pos, 0, 0, 0, False)
        self.addItem(flag)

    # Etabli un périmètre autour d'une case pour clean. ( drapeau et départ de team )
    def clearObstacleAroundPosition(self, position):
        for x in range(-1, 2):
            for y in range(-1, 2):
                pos = (position[0]+x, position[1]+y)
                if pos in self._plateau :
                    itemToRmv = self._plateau.pop(pos)
                    self._items.remove(itemToRmv)


