from datetime import datetime

def leser_datafil():
    with open("snoedybder_vaer_en_stasjon_dogn.csv", "r") as fil:
        linjer = fil.readlines()

    data_dict = {}

    for linje in linjer:
        linje = linje.strip().split(";")
        stasjons_data = {}

        stasjons_data["Dato"] = datetime.strptime(linje[2], "%d.%m.%Y")

        stasjons_data["Snodybde"] = linje[3]
        stasjons_data["Nedbor"] = linje[4]
        stasjons_data["Middeltemperatur"] = linje[5]
        stasjons_data["Skydekke"] = linje[6]
        stasjons_data["Hoyeste_middelvind"] = linje[7]

        år_nøkkel = stasjons_data["Dato"].year

        if år_nøkkel not in data_dict:
            data_dict[år_nøkkel] = []

        data_dict[år_nøkkel].append(stasjons_data)

    return data_dict
#Eksempel på bruk
print(leser_datafil()[2023][0]["Middeltemperatur"])
