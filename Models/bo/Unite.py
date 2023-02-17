# classe commune à toutes les unités
import random
from abc import ABC

from ProjectPiouPiou.Models.bo.Item import Item
from ProjectPiouPiou.Models.bo.Land import Land

from typing import Tuple


class Unite(Item, ABC):
    def __init__(self, name, equipe, position, mvt, pv, damage, vision, isDestructible = True):
        Item.__init__(self, name, equipe, position, isDestructible)
        self._mvt = mvt;
        self._pv = pv;
        self._damage = damage;
        self._vision = vision;

    # On veut de placer l'unité. On suppose les controles déjà fait précédemment
    def setPosition(self, coordonneesDestination : Tuple[float, float]):
        self._position = coordonneesDestination

    #chaque unité va avoir une maniere différente de se déplacer
    def seDeplacer(self, land : Land):
        mvtx = random.uniform(0, self._mvt)
        mvty = self._mvt - mvtx
        if random.uniform(0,1) > 0.5 :
            mvtx = mvtx * -1

        if random.uniform(0,1) > 0.5 :
            mvty = mvty * -1

        newPosi = (self._position[0]+mvtx, self._position[1]+mvty)
        if(land.isItemIsAtPos(newPosi)):

            self.setPosition(newPosi)






