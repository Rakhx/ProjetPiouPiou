import json
import requests
import ProjectPiouPiou.Models.bo.config as cg


class Client():

    def __init__(self, teamName):
        self._name = teamName
        # Position de départ
        r = requests.get("http://127.0.0.1:5000/init/register/"+teamName)
        received = json.loads(r.text)
        self._startPosition = tuple(int(i) for i in received[0])
        # Taille du terrain
        r = requests.get("http://127.0.0.1:5000/init/land")
        received = json.loads(r.text)
        self._tailleLand = tuple(int(i) for i in received[0])
        # Liste d'unités disponibles
        r = requests.get("http://127.0.0.1:5000/init/units")
        received = json.loads(r.text)
        self._unitDispos = tuple(i for i in received)

    # Enregistre une unité sur le serveur. Le serveur renvoi un message
    # OK = unité positionnée
    # ERR_EXIST = unité selectionnée n'existe pas ( faute de frappe? )
    # ERR_DISPO = unité selectionnée pas disponible
    # ERR_NAME = nom de l'unité déjà utilisé
    # ERR_PLACE = Positionnement de l'unité non disponible
    def registerUnit(self, unitType,unitName, pos):
        r = requests.get("http://127.0.0.1:5000/init/register?team=" + self._name + "&type=" + unitType +
                         "&name=" + unitName + self.posString(pos))
        return r.text

    def regarderAutour(self, unitName):
        r = requests.get("http://127.0.0.1:5000/loop/lookAround?team="+self._name + "&unitName=" + unitName)
        received = json.loads(r.text)
        return tuple(i for i in received)

    def deplacer(self, unitName, pos):
        r = requests.get("http://127.0.0.1:5000/loop/move?team="+self._name + "&unitName=" + unitName + self.posString(pos))
        return r.text

       # received = json.loads(r.text)
        #return tuple(i for i in received)

    def tirer(self, unitName, pos):
        pass

    def posString(self, pos):
        return "&posX=" + str(pos[0])+ "&posY=" + str(pos[1])

clicli = Client("TeamA")
print(clicli.registerUnit("Marines","Ultra", (1,1)))
print(clicli.registerUnit("Artilleur","piou", (0,0)))
print(clicli.regarderAutour("Ultra"))
print(clicli.deplacer("Ultra", (1,0)))

