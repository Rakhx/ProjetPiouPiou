# Classe qui correspond au terrain sur lequel se déroule la partie
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
        self._plateau.remove(item)

    def isItemIsAtPos(self, position : Tuple[float, float]) -> bool:
        for item in self._items :
            if item.isAtPosition(position) :
                return False

        return True


    # Une unité regarde autour d'elle
    def lookAround(self, position):
        retour = {}
        for x in range(-1,2):
            for y in range(-1,2):
                pos = (position[0]+x, position[1]+y)
                if pos in self._plateau:
                    retour[pos] = self._plateau[pos]
                    
        return retour

    # inverse le contenu du plateau pour pos1 et pos2
    def deplacerUnite(self, position1, position2):
        pass

