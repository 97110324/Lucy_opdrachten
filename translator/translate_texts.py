import os
from deep_translator import GoogleTranslator


def vraag_invoer():
    # Vraag om het pad naar de bronmap
    source_dir = input("Voer het pad naar de map met tekstbestanden in: ")
    if not os.path.exists(source_dir):
        print(f"Bronmap '{source_dir}' bestaat niet.")
        return None

    # Vraag om het pad naar de doelmap
    destination_dir = input("Voer het pad naar de map waar de vertaalde bestanden moeten worden opgeslagen: ")

    # Maak de doelmap als deze nog niet bestaat
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"Doelmap '{destination_dir}' is aangemaakt.")

    return source_dir, destination_dir


def vertaal_tekst(tekst, doeltaal="nl"):
    translator = GoogleTranslator(source="auto", target=doeltaal)
    vertaling = translator.translate(tekst)
    return vertaling


def vertaal_bestand(pad_naar_bestand, doel_dir, doeltaal="nl"):
    try:
        # Lees de inhoud van het bestand
        with open(pad_naar_bestand, "r", encoding="utf-8") as f:
            tekst = f.read()

        # Vertaal de tekst
        vertaling = vertaal_tekst(tekst, doeltaal)

        # Genereer het pad voor het vertaalde bestand
        bestandsnaam = os.path.basename(pad_naar_bestand)
        pad_naar_vertaald = os.path.join(doel_dir, bestandsnaam)

        # Sla de vertaling op in een nieuw bestand
        with open(pad_naar_vertaald, "w", encoding="utf-8") as f:
            f.write(vertaling)

        print(f"Bestand vertaald: {bestandsnaam}")
        return pad_naar_vertaald
    except Exception as e:
        print(f"Fout bij vertalen van {pad_naar_bestand}: {e}")
        return None


def verwerk_map(source_dir, destination_dir, doeltaal="nl"):
    vertaalde_bestanden = []

    # Doorloop alle bestanden in de bronmap
    for bestandsnaam in os.listdir(source_dir):
        pad_naar_bestand = os.path.join(source_dir, bestandsnaam)

        # Controleer of het een .txt-bestand is
        if bestandsnaam.endswith(".txt"):
            # Vertaal het bestand
            vertaald = vertaal_bestand(pad_naar_bestand, destination_dir, doeltaal)

            # Voeg het vertaalde bestand toe aan de lijst
            if vertaald:
                vertaalde_bestanden.append(vertaald)
        else:
            print(f"{bestandsnaam} wordt overgeslagen (geen .txt).")

    # Print de lijst van vertaalde bestanden
    print("\nLijst van vertaalde bestanden:")
    for bestand in vertaalde_bestanden:
        print(bestand)

    return vertaalde_bestanden


def main():
    # Vraag de gebruiker om invoer
    invoer = vraag_invoer()
    if invoer is None:
        return

    source_dir, destination_dir = invoer

    # Vertaal alle bestanden
    verwerk_map(source_dir, destination_dir, doeltaal="nl")


# Start het programma
if __name__ == "__main__":
    main()