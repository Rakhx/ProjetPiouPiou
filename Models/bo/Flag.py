from ProjectPiouPiou.Models.bo.Unite import Unite


class Flag(Unite):
    def __init__(self, *args):
        super().__init__(*args)

    def getShortClasse(self) -> str:
        return "F"

