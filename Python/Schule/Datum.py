Tag = 29
Monat = 2
Jahr = 2001

#! Falls Jahr größer als 2000 oder Monat größer als 12
#! oder der Tag größer als 30 ist Datum_ok Variable auf 0
#! Wenn nicht, Datum_ok Variable auf 1
if (Jahr < 2000) or (Monat > 12) or (Tag > 30):
    Datum_ok = 0
else:
    Datum_ok = 1

if Monat == 2 and Tag > 28:
    Datum_ok = 0

if (Datum_ok == 0):
    print("Das Datum ist Falsch!")
else:
    print("Das Datum ist richtig!")
