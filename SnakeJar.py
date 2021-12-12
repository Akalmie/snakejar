import random
print("Bienvenue dans le jeu !")
print("1 : facile, 2 : moyen, 3 : difficile")
level = int(input())
keyrings = 0
while keyrings != 3:
    print("Il y a 5 jarres devant vous. Choississez en une")
    snakes = ['S'] * level
    keys = ['K'] * (5 - level)
    jars = snakes + keys
    random.shuffle(jars)
    choix = int(input())
    print("Le joueur a mit la jarre n°", choix)
    if jars[choix-1] == 'K': 
        print("Gagné ! tu obtiens une clef magique ! La jarre infécté était", jars)
        keyrings += 1
        print("Tu as actuellement", keyrings, "/3 clefs")
        print("__________________")
    else:
        print("Perdu ! un serpent apparait !")
        print("__________________")
        if keyrings > 0:
            keyrings -= 1
            print("Tu as actuellement", keyrings, "/3 clefs")
            print("__________________")
print("Tu deviens le roi du temple !")