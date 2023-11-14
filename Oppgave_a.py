from datetime import datetime

def leser_datafil():
    with open("snoedybder_vaer_en_stasjon_dogn.csv", "r") as fil:
        linjer = fil.readlines()

    data_dict = {}

    for linje in linjer:
        linje = linje.strip().split(";")
        stasjons_data = {}

        stasjons_data["Dato"] = datetime.strptime(linje[2], "%d.%m.%Y")

        stasjons_data["Snodybde"] = int(linje[3]) if linje[3] != "-" else None
        stasjons_data["Nedbor"] = float(linje[4].replace(",", ".")) if linje[4] != "-" else None
        stasjons_data["Middeltemperatur"] = float(linje[5].replace(",",".")) if linje[5] != "-" else None
        stasjons_data["Skydekke"] = int(linje[7].replace(",",".")) if linje[7] != "-" else None
        stasjons_data["Hoyeste_middelvind"] = float(linje[7].replace(",",".")) if linje[7] != "-" else None

        år_nøkkel = stasjons_data["Dato"].year

        if år_nøkkel not in data_dict:
            data_dict[år_nøkkel] = []

        data_dict[år_nøkkel].append(stasjons_data)

    return data_dict

#Eksempel på bruk
#print(leser_datafil()[2023][0]["Middeltemperatur"])
