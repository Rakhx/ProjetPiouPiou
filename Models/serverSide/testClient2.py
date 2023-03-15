from ProjectPiouPiou.Models.serverSide.Client import Client

clientB = Client("TeamB")

print(clientB.registerUnit("Marines","marinesB", (30,30)))
print(clientB.registerUnit("Artilleur","artilleurB", (29,29)))

departM = 30

compteur = 0
while ( compteur < 5 ):
    etatBoard = clientB.newTurn()
    print(clientB.regarderAutour("marinesB"))
    departM = departM - 1
    print(clientB.deplacer("marinesB", (departM,30) ))
    compteur = compteur + 1

clientB.releasePriority()


#print(clientA.regarderAutour("Ultra"))
#print(clientA.deplacer("Ultra", (1,0)))

