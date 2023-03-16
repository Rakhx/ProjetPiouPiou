from ProjectPiouPiou.Models.serverSide.Client import Client


def moveToward(pos1, pos2):
    diffX = pos2[0] - pos1[0]
    diffY = pos2[1] - pos1[1]
    newPosX = pos1[0] + sign(diffX) * 1
    newPosY = pos1[1] + sign(diffY) * 1
    return newPosX, newPosY
def sign(value):
    if value > 0:
        return 1
    elif value < 0:
        return -1
    return 0


clientA = Client("TeamA")
print(clientA.registerUnit("Marines","Ultra", (1,1)))
print(clientA.registerUnit("Artilleur","piou", (2,2)))
posDep = (2,2)

compteur = 0
while compteur < 15:
    etatBoard = clientA.newTurn()
    #print(clientA.regarderAutour("Ultra"))
    compteur = compteur + 1
    retour = clientA.deplacer("piou", moveToward(posDep,(10,10)))
    if retour :
        posDep = moveToward(posDep,(10,10))

clientA.releasePriority()

