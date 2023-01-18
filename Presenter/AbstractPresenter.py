from abc import ABC, abstractmethod
import ProjectPiouPiou.View.AbstractView
from ProjectPiouPiou.Models.bo.Land import Land
from ProjectPiouPiou.View import AbstractView


class AbstractPresenter(ABC):

    # Quel que soit le presenter, il aura besoin d'une référence a la view
    def __init__(self ,  view : AbstractView):
        self._view = view

    @abstractmethod
    def parseLand(self, land : Land):
        pass
