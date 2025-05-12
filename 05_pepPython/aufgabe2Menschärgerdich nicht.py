import random  

zahl = random.randint(1, 6)

for versuch in range(1, 4):
    input("Drücke Enter zum würfeln {versuch}...")
    wurf = random.randint(1, 6)
    print("Du hast eine", wurf, "gewürfelt.")

    if wurf == 6:
        print("Glückwunsch! Du hast eine 6 gewürfelt. Würfel noch einmal und gehen dann so viele Felder")
        break 
else:
    print("\nDu hast keine 6 gewürfel, der nächste Spieler ist am Zug.")