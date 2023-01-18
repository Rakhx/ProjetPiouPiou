from ProjectPiouPiou.Models.Moteur import Moteur
from ProjectPiouPiou.Presenter.PresenterConsole import PresenterConsole
from ProjectPiouPiou.View.ConsoleView import ConsoleView
from ProjectPiouPiou.View.GuiView import GuiView

view = ConsoleView()
viewIHM = GuiView()
presenter = PresenterConsole(viewIHM)

model = Moteur(presenter)
model.go()

