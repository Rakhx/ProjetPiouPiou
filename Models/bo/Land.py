# Classe qui correspond au terrain sur lequel se déroule la partie
from typing import Tuple
from typing import List

from ProjectPiouPiou.Models.bo.Item import Item


class Land():
    def __init__(self, dimension : Tuple[float, float] = (), items : List[Item] = [] ):
        self._dimension = dimension
        self._items = items
        # initialise le plateau a vide
        self._plateau = [["-" for x in range(int(dimension[0]))] for y in range(int(dimension[1]))]

    def getDimension(self) -> Tuple[float, float]:
        return self._dimension

    def addItem(self, item : Item ):
        self._items.append(item)

    def removeItem(self, item : Item):
        pass

    def isItemIsAtPos(self, position : Tuple[float, float]) -> bool:
        for item in self._items :
            if item.isAtPosition(position) :
                return False

        return True


    # Une unité regarde autour d'elle
    def lookAround(self, position):
        pass

    # inverse le contenu du plateau pour pos1 et pos2
    def deplacerUnite(self, position1, position2):
        pass

