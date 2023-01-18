#Classe qui s'occupe du moteur de jeu
import time

from ProjectPiouPiou.Models.Initializer import Initializer
from ProjectPiouPiou.Models.bo.Land import Land
from ProjectPiouPiou.Models.bo.Item import Item

from typing import List

from ProjectPiouPiou.Models.bo.Obstacle import Obstacle
from ProjectPiouPiou.Models.bo.Unite import Unite
from ProjectPiouPiou.Presenter.AbstractPresenter import AbstractPresenter


class Moteur():

    def __init__(self, presenter : AbstractPresenter):
        # Utilisation des fonctions de lecture de données depuis fichier
        initit = Initializer()
        # Puis on la set
        self._land = Land(initit.getLandDimension(), initit.mockUnites())
        self._presenter = presenter

    def go(self):

        try:
            while True:
                print("boucle")
                self.boucle()
                self._presenter.parseLand(self._land)
                time.sleep(1)
        except KeyboardInterrupt:
            pass

    #fonction qui s'occupe des cycles du jeu
    def boucle(self):
        items = self._land.getItem()

        for item in items :
            # pour chaque
            if(isinstance(item, Unite)):
                item.seDeplacer(self._land)





