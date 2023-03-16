#Classe des obstacles, qui hérite d'item
from ProjectPiouPiou.Models.bo.Item import Item
from typing import Tuple

class Obstacle(Item):
    def __init__(self, position : Tuple[float, float], isDestructible=False):
        Item.__init__(self,"obstacle", "neutre", position, isDestructible)

    def getShortClasse(self) -> str:
        return 'O'

    def getPV(self) -> int:
        return -1
