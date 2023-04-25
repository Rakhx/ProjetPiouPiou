from ProjectPiouPiou.Models.bo.Artilleur import Artilleur
from ProjectPiouPiou.Models.bo.Base import Base
from ProjectPiouPiou.Models.bo.Eclaireur import Eclaireur
from ProjectPiouPiou.Models.bo.Flag import Flag
from ProjectPiouPiou.Models.bo.Marines import Marines
from ProjectPiouPiou.Models.bo.Item import Item
from ProjectPiouPiou.Models.bo.Land import Land
from ProjectPiouPiou.Models.bo.Obstacle import Obstacle
from ProjectPiouPiou.Presenter.AbstractPresenter import AbstractPresenter
from ProjectPiouPiou.View.AbstractView import AbstractView
from ProjectPiouPiou.View.ConsoleView import ConsoleView
import ProjectPiouPiou.Models.bo.config as cg



class PresenterConsole(AbstractPresenter):
    def __init__(self, view: AbstractView):
        AbstractPresenter.__init__(self, view)

    def parseLand(self, land: Land):
        # On ecrit une premiere fois le terrain sans prendre en compte
        # les item
        terrainAscii = ""
        posGetItem = False
        dimension = land.getDimension()
        for x in range(int(dimension[0])+1):
            for y in range(int(dimension[1])+1):

                for item in land.getItems():
                    if (item.isAtPosition((x, y))):
                        terrainAscii += self.getAsciiRepresentation(item)
                        posGetItem = True
                        break  # oui, oui...
                if (posGetItem):
                    posGetItem = False
                else:
                    terrainAscii += "-"
            terrainAscii += "\n"

        if not cg.viewGui:
            self._view.displayLand(terrainAscii)
        return terrainAscii

    def getAsciiRepresentation(self, item: Item) -> str:

        repr = item.getShortClasse()
        if (cg.equipes[item.getTeamName()] == 0):
            repr = repr.lower()

        # if (isinstance(item, Obstacle)):
        #
        #     repr = item.getShortRepresentation()
        # elif (isinstance(item, Artilleur)):
        #     repr = "A"
        # elif (isinstance(item, Marines)):
        #     if(cg.equipes[item.getTeamName()] == 0 ):
        #         repr = "M"
        #     else :
        #         repr = "m"
        # elif (isinstance(item, Eclaireur)):
        #     repr = "E"
        # elif (isinstance(item, Base)):
        #     repr = "B"
        # elif (isinstance(item, Flag)):
        #     repr = "F"

        return repr
