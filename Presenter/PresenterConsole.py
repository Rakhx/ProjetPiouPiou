from ProjectPiouPiou.Models.bo.Artilleur import Artilleur
from ProjectPiouPiou.Models.bo.Cible import Cible
from ProjectPiouPiou.Models.bo.Marines import Marines
from ProjectPiouPiou.Models.bo.Item import Item
from ProjectPiouPiou.Models.bo.Land import Land
from ProjectPiouPiou.Models.bo.Obstacle import Obstacle
from ProjectPiouPiou.Presenter.AbstractPresenter import AbstractPresenter
from ProjectPiouPiou.View.ConsoleView import ConsoleView


class PresenterConsole(AbstractPresenter):
    def __init__(self, view: ConsoleView):
        AbstractPresenter.__init__(self, view)

    def parseLand(self, land: Land):
        # On ecrit une premiere fois le terrain sans prendre en compte
        # les item
        terrainAscii = ""
        posGetItem = False
        dimension = land.getDimension()
        for x in range(int(dimension[0])):
            for y in range(int(dimension[1])):

                for item in land.getItem():
                    if(item.isAtPosition((x,y))):
                        terrainAscii += self.getAsciiRepresentation(item)
                        posGetItem = True
                        break # oui, oui...
                if(posGetItem):
                    posGetItem = False
                else :
                    terrainAscii += "-"
            terrainAscii += "\n"

        self._view.displayLand(terrainAscii)


    def getAsciiRepresentation(self, item : Item) -> str:

        repre = "-"
        if(isinstance(item, Obstacle)):
            repr = "o"
        elif(isinstance(item, Artilleur)):
            repr = "/"
        elif(isinstance(item, Marines)):
            repr= ">"
        elif(isinstance(item, Cible)):
            repr= "x"

        # else:
        #     repr = "'"

        return repr
