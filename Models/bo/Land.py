# Classe qui correspond au terrain sur lequel se déroule la partie
from typing import Tuple
from typing import List

from ProjectPiouPiou.Models.bo.Item import Item


class Land():
    def __init__(self, dimension : Tuple[float, float] = (), items : List[Item] = [] ):
        self._dimension = dimension
        self._items = items

    def setDimension(self, dimension : Tuple[float, float]):
        self._dimension = dimension

    def getDimension(self) -> Tuple[float, float]:
        return self._dimension

    def addItem(self, item : Item ):
        pass

    def getItem(self) -> List[Item]:
        return self._items.copy()

    def positionIsEmpty(self, position : Tuple[float, float]) -> bool:
        for item in self._items :
            if item.isAtPosition(position) :
                return False

        return True