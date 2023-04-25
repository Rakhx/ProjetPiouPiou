from ProjectPiouPiou.Models.bo.Unite import Item
import ProjectPiouPiou.Models.bo.config as cg

class Flag(Item):
    def getPV(self) -> int:
        return 1

    def __init__(self, *args):
        super().__init__(*args)
        self._picked = False
        self._bearer = None

    def getShortClasse(self) -> str:
        return "F"

    def bePickUp(self, aUnit):
        if cg.debug:
            print("Flag has been picked by ", aUnit.getName())
        self._picked = True
        self._bearer = aUnit
        #disapear

    def beDrop(self):
        self._picked = False
        self._bearer = None

    def isPicked(self):
        return self._picked

