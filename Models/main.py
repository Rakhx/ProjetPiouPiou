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

dic = {}
dic["un"] = "deux"
print(dic["un"])
par = "Deux"
try :
    res = dic[par]
    print(res)
except KeyError :
    print("clef existe pas")
    print("[MoteurFlask.regardeAutour({}) Clef n'existe pas".format( par))
    toto = "[MoteurFlask.regardeAutour({}) Clef n'existe pas".format(par)
    print(toto)

