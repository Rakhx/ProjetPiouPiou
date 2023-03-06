from ProjectPiouPiou.Models.bo.Artilleur import Artilleur
from ProjectPiouPiou.Models.bo.Marines import Marines
from ProjectPiouPiou.Models.bo.Eclaireur import Eclaireur
import ProjectPiouPiou.Models.bo.config as cg

class Team():

    def __init__(self, name, basePosition, land):
        self._name = name
        self._land = land

        # dic [nom, classe]
        self._units = {}
        self.basePosition = basePosition

        self._nbUnitRegistered = 0
        self._nbEclaireurRegistered = 0

    # Appelée au début du tour
    def newTurn(self):
        for key in self._units:
            self._units[key].resetTurn()

    # Verifie nom, position, & type.
    # TODO doit vérifier nombre d'unit en tout et nombre d'éclaireurs
    def registerUnit(self, type, name, posX, posY):
        posX = int(posX)
        posY = int(posY)
        position = (posX,posY)
        # position
        if (abs(posX-int(self.basePosition[0]) > 1) or abs(posY-int(self.basePosition[1]) > 1) ):
            return "ERR_PLACE"
        # nom
        if (self._units.__contains__(name)):
            return "ERR_NAME"
        # type
        try:
            dynamic_class = globals()[type]
            stats = getattr(cg,type)
            unit = dynamic_class(name, self._name,position, stats[0], stats[1], stats[2], stats[3])

        except BaseException as e:
            print(e.message)
            return "ERR_EXIST"

        self._units[name]= unit
        self._land.addItem(unit)
        return "FINE"

    def getUnitByName(self, unitName):
       # try :
            return self._units[unitName]
        #except KeyError:
         #   if cg.debug.debug:
          #      print("[Team.getUnitByName({}) Clef n'existe pas".format(unitName))
           # return "[Team.getUnitByName({}) Clef n'existe pas".format(unitName)