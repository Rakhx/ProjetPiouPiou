from ProjectPiouPiou.Models.bo.Artilleur import Artilleur
from ProjectPiouPiou.Models.bo.Marines import Marines
from ProjectPiouPiou.Models.bo.Eclaireur import Eclaireur
import ProjectPiouPiou.Models.bo.config as cg

class Team():

    def __init__(self, name, basePosition):
        self._name = name
        self._units = {}
        self.basePosition = basePosition

    # Verifie nom, position, & type
    def registerUnit(self, type, name, posX, posY):
        position = (posX,posY)
        # position
        if (abs(int(posX)-int(self.basePosition[0]) > 1) or abs(int(posY)-int(self.basePosition[1]) > 1) ):
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

        self._units[name]=(type, position)
        return "FINE"