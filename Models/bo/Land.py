# Classe qui correspond au terrain sur lequel se déroule la partie
import math
from typing import Tuple
from typing import List

from ProjectPiouPiou.Models.bo.Item import Item

class Land():
    def __init__(self, dimension : Tuple[float, float] = (), items : List[Item] = [] ):
        self._dimension = dimension
        self._items = items
        # initialise le plateau a vide
        self._plateau = {}
        for itemz in items:
            self._plateau[itemz.getPosition()] = itemz

    def getDimension(self) -> Tuple[float, float]:
        return self._dimension

    def addItem(self, item : Item ):
        self._items.append(item)
        self._plateau[item.getPosition()] = item

    def removeItem(self, item : Item):
        self._items.remove(item)
        self._plateau.pop(item)

    def getItemOrTrueAtPosition(self, position : Tuple[float, float]):
        if position in self._plateau:
            return self._plateau[position]
        return True

    def getCaseAtRange(self, position, range):
        pass

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
        for x in range(-1,portee+1):
            for y in range(-1,portee+1):
                if x != 0 or y != 0:
                    pos = (int(position[0])+int(x), int(position[1])+int(y))


                    if self.isAtCircleRange(position, pos, portee) and pos in self._plateau:
                        retour[pos] = self._plateau[pos]

        return retour

    # inverse le contenu du plateau pour pos1 et pos2
    def deplacerUnite(self, position1, position2):

        pass

    # retourne les positions directement connexe a la position
    def getPosConnexe(self, position):
        retour = []
        retour.append((position[0]+ 1, position[1]))
        retour.append((position[0]- 1, position[1]))
        retour.append((position[0], position[1]+ 1 ))
        retour.append((position[0], position[1]- 1 ))
        return retour

    # fonction récursive pour trouver les cases accessibles, en prennant en compte les obstacles
    def exploRecu(self, posOk, posPossible,currentPos,  range):
        range -= 1

        # for each case autour encore dans la liste des casePossible
        for position in self.getPosConnexe(currentPos):
            if(position in posPossible and position not in posOk):

                posOk.append(position)


                posPossible.remove(position)

            if(range > 0):
                self.exploRecu(posOk, posPossible, position, range)


