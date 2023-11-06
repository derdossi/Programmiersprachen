tag = 29
Monat = 2
Jahr = 2020

datumOk = 0

if Monat == 1 or Monat == 3 or Monat == 5 or Monat == 7 or Monat == 8 or \
        Monat == 10 or Monat == 12:
    if tag >= 1 and tag <= 31:
        datumOk = 1

if Monat == 4 or Monat == 6 or Monat == 9 or Monat == 11:
    if tag >= 1 and tag <= 30:
        datumOk = 1

if Monat == 2:
    if Jahr % 4 == 0:
        if tag >= 1 and tag <= 29:
            datumOk = 1
        else:
            if tag >= 1 and tag <= 28:
                datumOk = 1

if datumOk == 1:
    print("Das Datum ist korrekt!")
if datumOk == 0:
    print("Das Datum ist nicht korrekt!")
