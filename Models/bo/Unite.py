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
        self._shooted = False
        self._moved = False

    # On veut de placer l'unité. On suppose les controles déjà fait précédemment
    def setPosition(self, coordonneesDestination : Tuple[float, float]):
        self._position = coordonneesDestination

    def getPosition(self):
        return self._position

    def getRange(self):
        return self._vision

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

    # Fonction qui vérifie la possibilité pour une unité d'atteindre une position
    # Renvoi : OK si déplacement possible
    # NO_PRIS si la case est déja prise
    # NO_MVT si l'unité n'a pas assez de mouvement pour atteindre l'endroit
    def canReach(self, pos):
        pass

    def resetTurn(self):
        self._shooted = False;
        self._moved = False;

    def getPV(self) -> int:
        return self._pv
    def getDegat(self) -> int:
        return self._damage

    def takeShoot(self, degat):
        if self._isDestructible:
            self._pv = self._pv - degat
        return self._pv

    def moveToward(self, pos):
        diffX = self.getPosition()[0] - pos[0]
        diffY = self.getPosition()[1] - pos[1]
        newPosX = self.getPosition()[0] + self.sign(diffX) * 1
        newPosY = self.getPosition()[1] + self.sign(diffY) * 1
        return newPosX,newPosY


    def sign(self, value):
        if value > 0 :
            return 1
        elif value < 0 :
            return -1
        return 0
