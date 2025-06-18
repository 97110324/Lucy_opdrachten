from PIL import Image
import os
from fpdf import FPDF


def vraag_invoer():
    # Vraag om het pad naar de bronmap
    source_dir = input("Voer het pad naar de map met afbeeldingen in: ")
    if not os.path.exists(source_dir):
        print(f"Bronmap '{source_dir}' bestaat niet.")
        return None

    # Vraag om de naam van het uitvoer-PDF-bestand
    pdf_naam = input("Voer de naam van het uitvoer-PDF-bestand in (bijv. output.pdf): ")

    # Controleer of de extensie .pdf is
    if not pdf_naam.endswith(".pdf"):
        pdf_naam += ".pdf"

    return source_dir, pdf_naam


def is_jpg(bestandsnaam):
    _, extensie = os.path.splitext(bestandsnaam)
    return extensie.lower() == ".jpg"


def maak_pdf(source_dir, pdf_naam):
    # Maak een nieuw PDF-document
    pdf = FPDF()

    # Doorloop alle bestanden in de bronmap
    for bestandsnaam in os.listdir(source_dir):
        pad_naar_bestand = os.path.join(source_dir, bestandsnaam)

        # Controleer of het een .jpg-afbeelding is
        if is_jpg(bestandsnaam):
            # Laad de afbeelding
            img = Image.open(pad_naar_bestand)

            # Haal de breedte en hoogte van de afbeelding op
            breedte, hoogte = img.size

            # Converteer pixels naar millimeters (FPDF werkt met mm)
            breedte_mm = breedte / 0.264583333  # 1 inch = 72 pixels, 1 inch = 25.4 mm
            hoogte_mm = hoogte / 0.264583333

            # Voeg een nieuwe pagina toe met de juiste afmetingen
            pdf.add_page(orientation="P", format=(breedte_mm, hoogte_mm))

            # Voeg de afbeelding toe aan de pagina
            pdf.image(pad_naar_bestand, x=0, y=0, w=breedte_mm, h=hoogte_mm)

            print(f"Afbeelding toegevoegd: {bestandsnaam}")

    # Sla het PDF-bestand op
    pdf.output(pdf_naam, "F")
    print(f"PDF-bestand gemaakt: {pdf_naam}")


def main():
    # Vraag de gebruiker om invoer
    invoer = vraag_invoer()
    if invoer is None:
        return

    source_dir, pdf_naam = invoer

    # Maak het PDF-document
    maak_pdf(source_dir, pdf_naam)


# Start het programma
if __name__ == "__main__":
    main()