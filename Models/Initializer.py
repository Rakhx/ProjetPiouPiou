from typing import List, Tuple

from ProjectPiouPiou.Models.bo.Artilleur import Artilleur
from ProjectPiouPiou.Models.bo.Cible import Cible
from ProjectPiouPiou.Models.bo.Item import Item
from ProjectPiouPiou.Models.bo.Marines import Marines
from ProjectPiouPiou.Models.bo.Obstacle import Obstacle


# Classe qui va s'occuper d'initialiser les différents éléments du modèle
class Initializer:

    fileTerrain = "Terrain.txt"
    fileUnite = "unites.txt"
    unites = []


    # A la création de la classe, lecture automatique des fichiers textes
    def __init__(self):
        with open(self.fileTerrain, 'r') as lando:
            lignes = lando.readlines()
            i = 0

            for line in lignes :
                i = i + 1
                if i == 1 :
                    self.tailleTerrain = line
                if i == 2 :
                    self.placeDrapeau = line
                if i == 3 :
                    self.placeObstable = line.split(";")
                if i == 4 :
                    self.cible = line

        with open(self.fileUnite, 'r') as unito :
            lignes = unito.readlines()
            for line in lignes:
                self.unites.append(line)


    # On lit la taille du terrain
    def mockLand(self) -> Tuple[float, float]:
        pass

    # On prend la dimension du terrain
    def getLandDimension(self):
        self.tailleTerrain = tuple(self.tailleTerrain.split("x"))
        return self.tailleTerrain

    # devrait faire de la lecture de fichier
    # On lit un fichier texte qui contient les unités
    # la fonction nous renvoi une liste d'item
    def mockUnites(self) -> List[Item] :
        listItem = []


        return self.getUnites()


    # Récupération des obstacles, des unités, des cibles
    def getUnites(self):
        listItem = []

        # unites
        listItem += [Marines((3.0, 4), 1, 1, 1, 1)]
        listItem += [Artilleur("autres", (6.0, 5), 1, 1, 1, 1)]
        for typeUnit in self.unites :
            pass


            # # separe nombre et autre
            # read = typeUnit.split(":")
            # # separe detail sur unite
            # detail = read[1].split(',')
            #
            # # on crée X fois un nombre d'unités du meme type
            # for i in range(int(read[0]) + 1):
            #     #Obtenir la classe depuis une chaine de char
            #     #cls = globals()[detail[-1].replace("\n", "")
            #     pass

        #obstacle
        for obs in self.placeObstable:
            obs = obs.split('x')
            listItem += [Obstacle( ( int(obs[0]), int(obs[1])))]

        # cible
        pos = self.cible.split("x")
        listItem += [Cible(( int(pos[0]), int(pos[1])), 0, 1, 0, 0 )]

        return listItem



    def readFile(self):
        pass