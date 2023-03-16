from ProjectPiouPiou.Models.bo.Unite import Unite


class Flag(Unite):
    def getShortClasse(self) -> str:
        return "F"

    def __init__(self, *args):
        super().__init__(*args)

