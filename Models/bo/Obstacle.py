#Classe des obstacles, qui hérite d'item
from ProjectPiouPiou.Models.bo.Item import Item
from typing import Tuple

class Obstacle(Item):
    def __init__(self, position : Tuple[float, float], isDestructible : bool = False):
        Item.__init__(self, position, isDestructible)
