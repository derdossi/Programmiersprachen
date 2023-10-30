import csv


brutto = 2003
steuerklasse = 3

with open("csv datei") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    for row in readCSV:
        if brutto >= int(row[0]) and brutto < int (row[0])+3:
            lohnsteuer = float(row[steuerklasse])


