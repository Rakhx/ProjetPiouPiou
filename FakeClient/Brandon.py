from ProjectPiouPiou.FakeClient.MockClient import MockClient
from ProjectPiouPiou.Models.bo.Artilleur import Artilleur
from ProjectPiouPiou.Models.bo.Eclaireur import Eclaireur
from ProjectPiouPiou.Models.bo.Land import Land
from ProjectPiouPiou.Models.bo.Marines import Marines



# l'innocence

client = MockClient("létrofor")
basePosition = client.startPosition
tailleTerrain = client.tailleLand
unitesDispos = client.unitDispos

mesUnites = []

posX = basePosition[0]
posY = basePosition[1]
stats = unitesDispos[0].split(':')[1].split(',')
# génération d'unité
mar1 = Marines("ultra1", "létrofor",( posX-1, posY - 1), stats[0], stats[1], stats[2], stats[3] )
client.registerUnit("Marines","ultra1", ( posX-1, posY - 1) )
mar2 = Marines("ultra2", "létrofor",( posX+1, posY + 1), stats[0], stats[1], stats[2], stats[3] )
client.registerUnit("Marines","ultra2", ( posX+1, posY + 1) )
stats = unitesDispos[1].split(':')[1].split(',')
art1 = Artilleur("arti1", "létrofor",( posX-1, posY + 1), stats[0], stats[1], stats[2], stats[3] )
client.registerUnit("Artilleur","arti1", ( posX-1, posY + 1) )
stats = unitesDispos[2].split(':')[1].split(',')
eclai1 = Eclaireur("eclai1", "létrofor",( posX+1, posY - 1), stats[0], stats[1], stats[2], stats[3] )
client.registerUnit("Eclaireur","eclai1", (  posX+1, posY - 1) )
mesUnites.append(mar1)
mesUnites.append(mar2)
mesUnites.append(art1)
mesUnites.append(eclai1)


# boucle de jeu
continuer = True
compteur = 0
while continuer :
    client.newTurn()

    compteur = compteur +1
    if compteur > 20 :
        continuer = False

