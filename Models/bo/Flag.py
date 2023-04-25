from ProjectPiouPiou.Models.bo.Unite import Unite


class Flag(Unite):
    def __init__(self, *args):
        super().__init__(*args)
        self._picked = False
        self._bearer = None

    def getShortClasse(self) -> str:
        return "F"

    def bePickUp(self, aUnit):
        self._picked = True
        self._bearer = aUnit

    def beDrop(self):
        self._picked = False
        self._bearer = None

    def isPicked(self):
        return self._picked

