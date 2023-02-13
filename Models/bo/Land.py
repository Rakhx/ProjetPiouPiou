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


    def setDimension(self, dimension : Tuple[float, float]):
        self._dimension = dimension

    def getDimension(self) -> Tuple[float, float]:
        return self._dimension

    def addItem(self, item : Item ):
        pass

    def getItem(self) -> List[Item]:
        return self._items.copy()

    def isItemIsAtPos(self, position : Tuple[float, float]) -> bool:
        for item in self._items :
            if item.isAtPosition(position) :
                return False

        return True

    # regarde le plateau et vérifie qu'il est disponible ou non
    def isPositionEmpty(self, position):
        if (self._plateau[position[0]][position[1]] == "-"):
            return True;
        return False;

    # inverse le contenu du plateau pour pos1 et pos2
    def deplacerUnite(self, position1, position2):
        pass

