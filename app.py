def erstelle_brett():
    brett = []
    for i in range(3):
        brett.append([" ", " ", " "])
    return brett


def drucke_brett(brett):
    for zeile in brett:
        print("|".join(zeile))
        print("-----")


def mache_zug(brett, spieler, zeile, spalte):
    if brett[zeile][spalte] == " ":
        brett[zeile][spalte] = spieler
        return True
    return False


def hat_gewonnen(brett, spieler):
    # Zeilen
    for zeile in brett:
        if zeile[0] == spieler and zeile[1] == spieler and zeile[2] == spieler:
            return True

    # Spalten
    for spalte in range(3):
        if brett[0][spalte] == spieler and brett[1][spalte] == spieler and brett[2][spalte] == spieler:
            return True

    # Diagonalen
    if brett[0][0] == spieler and brett[1][1] == spieler and brett[2][2] == spieler:
        return True

    if brett[0][2] == spieler and brett[1][1] == spieler and brett[2][0] == spieler:
        return True

    return False


def spiele_tic_tac_toe():
    brett = erstelle_brett()
    aktueller_spieler = "X"

    while True:
        drucke_brett(brett)

        # Eingabe abfangen
        try:
            zeile = int(input(f"Spieler {aktueller_spieler}, Zeile (0-2): "))
            spalte = int(input(f"Spieler {aktueller_spieler}, Spalte (0-2): "))
        except ValueError:
            print("Ungültige Eingabe. Bitte Zahlen von 0 bis 2 eingeben.")
            continue

        # Bereich prüfen
        if zeile < 0 or zeile > 2 or spalte < 0 or spalte > 2:
            print("Ungültige Zeile oder Spalte. Nochmal versuchen.")
            continue

        # Zug versuchen
        if not mache_zug(brett, aktueller_spieler, zeile, spalte):
            print("Feld bereits belegt. Nochmal versuchen.")
            continue

        # Gewinn prüfen
        if hat_gewonnen(brett, aktueller_spieler):
            drucke_brett(brett)
            print(f"Spieler {aktueller_spieler} hat gewonnen!")
            break

        # Spieler wechseln
        aktueller_spieler = "O" if aktueller_spieler == "X" else "X"


spiele_tic_tac_toe()


