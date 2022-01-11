import pandas as pd
import random

vakken = pd.read_csv("vakken.csv", sep=";")
zalen = pd.read_csv("zalen.csv", sep=";")
print(zalen)
print(vakken)

tijdsslots = []
for dag in ["ma", "di", "wo", "do", "vr"]:
    for tijd in ["9-11", "11-13", "13-15", "15-17"]:
        tijdsslots.append(dag + tijd)


# maak een lijst van zaalslots
zaalslots = []
for zaal in zalen["zaal"]:
    for tijd in tijdsslots:
        zaalslots.append((zaal, tijd))

alle_colleges = []

for index, vak in vakken.iterrows():
    for i in range(vak["hoorcolleges"]):
        alle_colleges.append((vak["vak"], "HC"))
    for i in range(vak["werkcolleges"]):
        alle_colleges.append((vak["vak"], "WC"))
    for i in range(vak["practica"]):
        alle_colleges.append((vak["vak"], "P"))

# Kies random 72 zaalslots
random_zaalslots = random.sample(zaalslots, 72)

rooster = []

for i in range(72):
    rooster.append(alle_colleges[i] + random_zaalslots[i])

print(rooster)











