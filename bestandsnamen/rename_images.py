import os


def hoofd_menu():
    print("Welkom bij de Bestandshernoemer!")
    print("Kies een optie:")
    print("1. Lijst van bestanden opslaan")
    print("2. Bestanden hernoemen")
    print("3. Terug naar originele namen")

    keuze = input("Typ 1, 2 of 3: ")

    if keuze == "1":
        maak_bestandslijst()
    elif keuze == "2":
        hernoem_bestanden()
    elif keuze == "3":
        zet_terug_naar_origineel()
    else:
        print("Foutieve keuze!")


def maak_bestandslijst():
    mapnaam = input("Typ de mapnaam waar de afbeeldingen staan (bijv. posters): ")
    try:
        namen = os.listdir(mapnaam)
        with open("oude_namen.txt", "w") as f:
            for naam in namen:
                f.write(naam + "\n")
        print("Oude namen opgeslagen in 'oude_namen.txt'")
    except:
        print("Map niet gevonden.")


def hernoem_bestanden():
    mapnaam = input("Typ de mapnaam waar de afbeeldingen staan: ")
    try:
        namen = sorted(os.listdir(mapnaam))
        for i, naam in enumerate(namen, start=1):
            extensie = os.path.splitext(naam)[1]
            nieuwenaam = f"movie_poster_{i:02}{extensie}"
            oud_pad = os.path.join(mapnaam, naam)
            nieuw_pad = os.path.join(mapnaam, nieuwenaam)
            os.rename(oud_pad, nieuw_pad)
            print(f"Hernoemd: {naam} → {nieuwenaam}")
    except:
        print("Er ging iets fout bij hernoemen.")


def zet_terug_naar_origineel():
    mapnaam = input("Typ de mapnaam waar de afbeeldingen staan: ")
    try:
        with open("oude_namen.txt", "r") as f:
            originelen = [line.strip() for line in f.readlines()]
        huidige = sorted(os.listdir(mapnaam))
        if len(originelen) != len(huidige):
            print("Aantal bestanden komt niet overeen.")
            return
        for oud, nieuw in zip(huidige, originelen):
            oud_pad = os.path.join(mapnaam, oud)
            nieuw_pad = os.path.join(mapnaam, nieuw)
            os.rename(oud_pad, nieuw_pad)
            print(f"Hersteld: {oud} -> {nieuw}")
            print("Bestanden zijn teruggezet naar originele namen.")
    except Exception as e:
        print("Kon namen niet herstellen:", e)


# Start het programma
hoofd_menu()