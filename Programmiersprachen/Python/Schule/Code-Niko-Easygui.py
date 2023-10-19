from easygui import *
text = ("Geben sie den Bruttolohn ein")
title = ("Aufgabe Nettolohnberechnung")
output = enterbox(text, title)

# Eingabe
bruttolohn = float(output)

# Berechnung der einzelnen Versicherungskosten
krankenversicherung = (bruttolohn*0.146)*0.5
rentenversicherung = (bruttolohn*0.186)*0.5
arbeitslosenversicherung = (bruttolohn*0.034)*0.5
pflegeversicherung = (bruttolohn*0.026)*0.5

if bruttolohn > 5000:
    lohnsteuer = bruttolohn * 0.35
elif bruttolohn > 4000 and bruttolohn < 5001:
    lohnsteuer = bruttolohn * 0.30
elif bruttolohn > 3000 and bruttolohn < 4001:
    lohnsteuer = bruttolohn * 0.25
else:
    lohnsteuer = bruttolohn * 0.20

kirchensteuer = (lohnsteuer*0.080)

# Berechnung Nettolohn
nettolohn = bruttolohn-krankenversicherung-rentenversicherung - \
    arbeitslosenversicherung-pflegeversicherung-lohnsteuer-kirchensteuer


text1 = ("Bruttolohn:               " + str(bruttolohn))
text2 = ("Krankenversicherung:     - " + str(krankenversicherung))
text3 = ("Rentenversicherung:      - " + str(rentenversicherung))
text4 = ("Arbeitslosenversicherung:-  " + str(arbeitslosenversicherung))
text5 = ("Pflegeversicherung:      -  " + str(pflegeversicherung))
text6 = ("Lohnsteuer:              -" + str(lohnsteuer))
text7 = ("Kirchensteuer:           - " + str(kirchensteuer))
text8 = "---------------------------------"
text9 = ("Nettolohn:                " + str(nettolohn))
title1 = ("Ausgabe")
text10 = text1, "\n", text2, "\n", text3, "\n", text4, "\n", text5, "\n", text6, "\n", text7, "\n", text8, "\n", text9
output = textbox("Ihre Nettorechnung lautet", title1, text10)
# Ausgabe
print("Bruttolohn:               ", bruttolohn)
print("Krankenversicherung:     - ", krankenversicherung)
print("Rentenversicherung:      - ", rentenversicherung)
print("Arbeitslosenversicherung:-  ", arbeitslosenversicherung)
print("Pflegeversicherung:      -  ", pflegeversicherung)
print("Lohnsteuer:              -", lohnsteuer)
print("Kirchensteuer:           - ", kirchensteuer)
print("---------------------------------")
print("Nettolohn:                ", nettolohn)
