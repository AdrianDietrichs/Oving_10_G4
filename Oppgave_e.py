from datetime import datetime
from Oppgave_a import leser_datafil
from Del_1_h import VoksendePlante
import matplotlib.pyplot as plt

def filtrer_gyldige_år(data_dict):
    gyldige_år = []

    for år, værdata in data_dict.items():
        antall_temperatur_dager = sum(1 for dag in værdata if dag["Middeltemperatur"] is not None or "-")

        if antall_temperatur_dager >= 300:
            gyldige_år.append(år)

    return gyldige_år

def beregn_og_skriv_vekst(data_dict):
    gyldige_år = filtrer_gyldige_år(data_dict)
    vekstresultater = []  # Lagrer vekstresultatene her

    for år in gyldige_år:
        værdata_for_år = data_dict[år]
        temperatur_data_for_år = [dag["Middeltemperatur"] for dag in værdata_for_år if dag["Middeltemperatur"] is not None]

        vekst_resultat = VoksendePlante(temperatur_data_for_år)
        vekstresultater.append(vekst_resultat)  # Legg til resultatene i listen

    # Plotting av vekstresultatene
    årstall = gyldige_år
    plt.plot(årstall, vekstresultater, marker='o', linestyle='-', color='b')
    plt.show()

data_dict = leser_datafil()
beregn_og_skriv_vekst(data_dict)
