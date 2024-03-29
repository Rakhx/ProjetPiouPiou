# Classe de base qui sera commnune à toutes les éléments présents sur la map
import math

from typing import Tuple
from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, equipe, position : Tuple[float, float], isDestructible : bool):
        self._position = position
        self._isDestructible = isDestructible
        self._camp = equipe
        self._name = name

    def getPosition(self) -> Tuple[float, float]:
        return self._position

    def setPosition(self, position):
        self._position = position

    # Vérifie si l'item se trouve "autour" de la position en parametre
    def isAtPosition(self, position : Tuple[float, float]) -> bool:
        if (abs(self._position[0] - position[0]) <= 0.5) and (abs(self._position[1] - position[1]) <= 0.5) :
            return True
        return False

    # obtenir la distance entre l'item courant et une position cible
    def getDistance(self, positionCible : Tuple[float, float]) -> float:
        return math.sqrt(math.pow(self._position[0]-positionCible[0],2) +
               +          math.pow(self._position[1]-positionCible[1],2))

    # Return le nom donné au début
    def getName(self):
        return self._name

    # Renvoi lettre pour le type de l'unité, ainsi que les pv restant. Si pv infini, -1
    def getShortRepresentation(self):
        return (self.getShortClasse(), self.getPV())

    @abstractmethod
    def getShortClasse(self) -> str:
        pass

    @abstractmethod
    def getPV(self) -> int:
        pass

    # est redéfini dans les unités, sert ici pour Flag & obstable
    def takeShoot(self, degat):
        return 1

    def getTeamName(self):
        return self._camp
