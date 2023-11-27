import datetime
brutto = 1000

if brutto > 5000:
    netto = brutto*0.35
elif brutto > 4000 and brutto <= 5000:
    netto = brutto * 0.3
elif brutto > 3000 and brutto <= 4000:
    netto = brutto * 0.25
elif brutto <= 3000:
    netto = brutto*0.2

# Aufg. 2
# if brutto > 5000:
#     netto = brutto*0.35
#
# elif brutto > 3000 and brutto <= 4000:
#     netto = brutto * 0.25
# elif brutto <= 3000:
#     netto = brutto*0.2
#! elif brutto > 4000 or brutto <= 5000:
#!     netto = brutto * 0.3


# Aktuelles Datum
heute = datetime.date.today()

# Nächstes JHV Datum
naechstes_jhv = datetime.date(heute.year, 10, 1)

# Wenn das nächste JHV bereits vorbei ist, dann setze es auf das JHV im nächsten Jahr
if heute > naechstes_jhv:
    naechstes_jhv = datetime.date(heute.year + 1, 10, 1)

# Berechne die Tage bis zum nächsten JHV
countdown = (naechstes_jhv - heute).days

print("Tage bis zur nächsten Jahreshauptversammlung des FC Nordstadt:", countdown)

km = 110

if km <= 10:
    bezahlung = 1.20*km + 3
if km > 10 and km < 20:
    bezahlung = 10*1.20 + (km-10)*0.9 + 3
if km > 20:
    bezahlung = 10*1.20 + (km-10)*0.9
