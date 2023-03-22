#Classe des obstacles, qui hérite d'item
from ProjectPiouPiou.Models.bo.Item import Item
from typing import Tuple

class Base(Item):
    def __init__(self, position : Tuple[float, float], team ,isDestructible=False):
        Item.__init__(self,"base", team, position, isDestructible)

    def getShortClasse(self) -> str:
        return 'B'

    def getPV(self) -> int:
        return -1
