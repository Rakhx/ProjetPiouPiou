from ProjectPiouPiou.Models.bo.Item import Item
from typing import Tuple

from ProjectPiouPiou.Models.bo.Unite import Unite


class Marines(Unite):
    def __init__(self, position, mvt, pv, damage, vision, name, camp):
        Unite.__init__(self, position, mvt, pv, damage, vision, name, camp)

