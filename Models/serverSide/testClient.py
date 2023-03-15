from ProjectPiouPiou.Models.serverSide.Client import Client

clientA = Client("TeamA")
print(clientA.registerUnit("Marines","Ultra", (1,1)))
print(clientA.registerUnit("Artilleur","piou", (0,0)))

print(clientA.regarderAutour("Ultra"))

compteur = 0
while ( compteur < 5 ):
    etatBoard = clientA.newTurn()
    print(clientA.regarderAutour("Ultra"))
    compteur = compteur + 1

clientA.releasePriority()
