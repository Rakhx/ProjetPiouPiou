tailleTerrainTuple = (20, 20)

# Deplacement, pv , degat, vision
Marines = (2, 5, 4, 2)
Artilleur = (1, 2, 3, 3)
Eclaireur = (4, 1, 0, 5)

# Temps d'arrêt entre le relachement de priorité et la demande pour le cycle suivant
sleepTimeSc = 5
debug = True
viewGui = False
equipes = {}
equipes["Neutre"] = -1


def fromListTodic(toConvert):
    result = {}
    tupleEnPlus = []
    count = 0
    for tuples in toConvert:
        if len(tuples) > 0:
            count = 0
            tupleEnPlus.clear()
            for element in tuples:
                if count == 0:
                    pos = element
                else:
                    tupleEnPlus.append(element)
                count = count + 1

            result[pos] = tuple(tupleEnPlus)

    return result
