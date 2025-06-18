from PIL import Image
import os


def vraag_invoer():
    # Vraag om maximale grootte
    max_grootte = int(input("Voer het maximale formaat in (maximaal 2000 pixels): "))

    # Controleer of de maximale grootte geldig is
    if max_grootte > 2000:
        print("Maximale grootte mag niet groter zijn dan 2000 pixels.")
        return None

    # Vraag om pad naar bronmap
    source_dir = input("Voer het pad naar de bronmap in: ")
    if not os.path.exists(source_dir):
        print(f"Bronmap '{source_dir}' bestaat niet.")
        return None

    # Vraag om pad naar doelmap
    destination_dir = input("Voer het pad naar de doelmap in: ")
    if not os.path.exists(destination_dir):
        print(f"Doelmap '{destination_dir}' bestaat niet.")
        return None

    return max_grootte, source_dir, destination_dir


def is_afbeelding(bestandsnaam):
    extensies = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}
    _, extensie = os.path.splitext(bestandsnaam)
    return extensie.lower() in extensies


def verklein_afbeelding(pad_naar_bestand, max_grootte):
    try:
        # Laad de afbeelding
        img = Image.open(pad_naar_bestand)

        # Bereken het nieuwe formaat
        breedte, hoogte = img.size
        if breedte > hoogte:
            nieuwe_breedte = max_grootte
            nieuwe_hoogte = int((hoogte / breedte) * max_grootte)
        else:
            nieuwe_hoogte = max_grootte
            nieuwe_breedte = int((breedte / hoogte) * max_grootte)

        # Resize de afbeelding
        img_resized = img.resize((nieuwe_breedte, nieuwe_hoogte), Image.LANCZOS)

        # Geef feedback
        print(f"Afbeelding verkleind: {pad_naar_bestand} -> {nieuwe_breedte}x{nieuwe_hoogte}")

        return img_resized
    except Exception as e:
        print(f"Fout bij verkleinen van {pad_naar_bestand}: {e}")
        return None


def verwerk_afbeeldingen(source_dir, destination_dir, max_grootte):
    # Teller voor het aantal afbeeldingen
    teller = 0

    # Doorloop alle bestanden in de bronmap
    for bestandsnaam in os.listdir(source_dir):
        pad_naar_bestand = os.path.join(source_dir, bestandsnaam)

        # Controleer of het een afbeelding is
        if is_afbeelding(bestandsnaam):
            # Verklein de afbeelding
            img_resized = verklein_afbeelding(pad_naar_bestand, max_grootte)

            # Bewaar de verkleinde afbeelding in de doelmap
            if img_resized:
                pad_naar_doel = os.path.join(destination_dir, bestandsnaam)
                img_resized.save(pad_naar_doel)
                teller += 1
        else:
            print(f"{bestandsnaam} wordt overgeslagen (geen afbeelding).")

    # Print het totaal aantal verwerkte afbeeldingen
    print(f"Totaal {teller} afbeeldingen verwerkt.")


def main():
    # Vraag de gebruiker om invoer
    invoer = vraag_invoer()
    if invoer is None:
        return

    max_grootte, source_dir, destination_dir = invoer

    # Verwerk de afbeeldingen
    verwerk_afbeeldingen(source_dir, destination_dir, max_grootte)


# Start het programma
if __name__ == "__main__":
    main()