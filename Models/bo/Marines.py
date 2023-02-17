from ProjectPiouPiou.Models.bo.Item import Item
from typing import Tuple

from ProjectPiouPiou.Models.bo.Unite import Unite


class Marines(Unite):
    def __init__(self, name, equipe, position, mvt, pv, damage, vision):
        Unite.__init__(self, name, equipe, position, mvt, pv, damage, vision)

