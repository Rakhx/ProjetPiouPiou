from ProjectPiouPiou.Models.bo.Land import Land
from ProjectPiouPiou.Presenter.AbstractPresenter import AbstractPresenter
from ProjectPiouPiou.View.GuiView import GuiView
import threading
from tkinter import *

class GuiPresenter(AbstractPresenter):

    def __init__(self, view : GuiView):
        super().__init__(view)


    # Fonction qui prend un objet de type land en parametre et le prépare pour affichage dans la vue GUI
    def parseLand(self, land: Land):

        pass

