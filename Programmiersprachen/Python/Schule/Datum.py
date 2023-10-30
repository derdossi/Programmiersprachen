Tag = 20
Monat = 5
Jahr = 2001
Datum_ok = 1


if (Jahr < 2000) or (Monat > 12) or (Tag > 30):
    Datum_ok = 0
if Monat == 2 and Tag > 28:
    Datum_ok = 0
if (Datum_ok == 0):
    print("Das Datum ist Falsch!")
else:
    print("Das Datum ist richtig!")
