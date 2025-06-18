import pandas as pd
import matplotlib.pyplot as plt

# Laad data
branches = pd.read_csv("branches.csv")
bedrijven = pd.read_csv("bedrijven.csv")

# Combineer data
data = pd.merge(bedrijven, branches, on="idbranch")

# Tel aantal bedrijven per branche
aantal_per_branche = data["omschrijving"].value_counts()

# Toon staafdiagram
aantal_per_branche.plot(kind="bar", title="Aantal bedrijven per branche")
plt.xlabel("Branche")
plt.ylabel("Aantal bedrijven")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()