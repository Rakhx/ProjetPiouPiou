import math

from ProjectPiouPiou.Models.bo.Item import Item
from ProjectPiouPiou.Models.bo.Unite import Unite


class Artilleur(Unite):
    def __init__(self,ajout, *args ):
        super().__init__(*args)
        self._ajout = ajout
