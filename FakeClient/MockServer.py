from ProjectPiouPiou.Models.serverSide.MoteurFlask import MoteurFlask
import ProjectPiouPiou.Models.bo.config as cg

class MockServer:

    def __init__(self):
        self._moteur = MoteurFlask()

    # --------------------------------------
    #   Initialisation de début de game
    # --------------------------------------

    # Register le nom de la team, return la position du drapeau de départ
    def registerTeam(self, name):
        return convertToString(self._moteur.registerTeam(name))

    def registerUnit(self, request):
        test = request
        message = self._moteur.registerUnite(test["team"], test["type"], test["name"], test["posX"], test["posY"])
        if cg.debug:
            print("Register unit ", test["name"], "de type: ", test["type"], " pour team", test["team"],
                  " position ", test["posX"], "x", test["posY"], ":", message)

        return message

    # --------------------------------------
    #   Boucle en cours de  game
    # --------------------------------------

    # regarde autour
    def regarderAutour(self, param):
        return [tuple(str(x) for x in self._moteur.regardeAutour(param["team"], param["unitName"]))]

    def deplacementUnite(self, param):
        return self._moteur.deplacementUnite(param["team"], param["unitName"], (int(param["posX"]), int(param["posY"])))

    def tirer(self, param):
        return self._moteur.shoot(param["team"], param["unitName"], (int(param["posX"]), int(param["posY"])))

    # --------------------------------------
    # Mutex stuff
    # --------------------------------------
    def getPriority(self, param):
        teamWithPrio = param["team"]
        if cg.debug:
            print("equipe " + param["team"] + " prend la priorite")
        representation = self._moteur.displayLand()

        #modifyValue(representation)

        return self._moteur.sumupSituation(param["team"])


    def sumUpSituaiton(self, param):
        teamWithPrio = param["team"]
        # if cg.debug:
        #     print("equipe " + param["team"] + " prend la priorite")
        # representation = self._moteur.displayLand()
        #
        # # modifyValue(representation)

        return self._moteur.sumupSituation(param["team"])

def convertToString(value):
    return [tuple(str(x) for x in value)]