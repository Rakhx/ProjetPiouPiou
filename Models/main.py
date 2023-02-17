from ProjectPiouPiou.Models.Moteur import Moteur
from ProjectPiouPiou.Presenter.PresenterConsole import PresenterConsole
from ProjectPiouPiou.View.ConsoleView import ConsoleView
from ProjectPiouPiou.View.GuiView import GuiView
from ProjectPiouPiou.Models.bo.Marines import Marines
import ProjectPiouPiou.Models.bo.config  as cg
view = ConsoleView()
viewIHM = GuiView()
presenter = PresenterConsole(viewIHM)

#model = Moteur(presenter)
#model.go()



#newobject = dynamic_class()
try:
    dynamic_class = globals()["Marines"]
    stats = getattr(cg, "Marnes")
    unit = dynamic_class("Marines", "self._name", (1,1), stats[0], stats[1], stats[2], stats[3])
except BaseException as e:
    print("marche pas ")

