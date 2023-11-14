from datetime import datetime
from Oppgave_a import leser_datafil
from Del_1_e import differanse

import matplotlib.pyplot as plt

def gjennomsnittstemperaturer(data_dict):
    gjennomsnittstemperaturer = {}
    for år, værdata in data_dict.items():
        for dag in værdata:
            måned_år = dag["Dato"].strftime("%B %Y")  # Konverterer til måned og år
            temperatur = dag["Middeltemperatur"]
            if temperatur != "-" and temperatur is not None:
                if måned_år not in gjennomsnittstemperaturer:
                    gjennomsnittstemperaturer[måned_år] = [float(temperatur)]
                else:
                    gjennomsnittstemperaturer[måned_år].append(float(temperatur))

    gjennomsnitt_for_måned = {måned_år: sum(temp) / len(temp) for måned_år, temp in gjennomsnittstemperaturer.items()}
    return gjennomsnitt_for_måned

data_dict = leser_datafil()
gjennomsnitt_for_måned = gjennomsnittstemperaturer(data_dict)

gjennomsnittsliste = list(gjennomsnitt_for_måned.values())
måned_år = list(gjennomsnitt_for_måned.keys())

# Konverter måned-år-strenger til numeriske verdier (for eksempel månednummer eller årstall)
numeriske_måneder_år = [datetime.strptime(dato, "%B %Y").month for dato in måned_år]

# Pass de numeriske verdiene til differanse-funksjonen
differanser = differanse(numeriske_måneder_år, gjennomsnittsliste)

# Filtrer ut None-verdier fra differansene før plotting
filtrerte_differanser = [diff for diff in differanser if diff is not None]

plt.plot(måned_år[1:], filtrerte_differanser, label="Differanser")
plt.show()