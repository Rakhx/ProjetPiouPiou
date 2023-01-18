from abc import ABC, abstractmethod

# Classe commune à toutes les vues
class AbstractView(ABC):

    @abstractmethod
    def displayLand(self, situation):
        pass
