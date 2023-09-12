import re

bezugspreis = float(input(" Geben Sie den Bezugspreis ein:"))

# Berechnung des Listenverkaufspreis/Brutto
handelskosten = (bezugspreis / 100 * 25)
selbstkostenpreis = bezugspreis + handelskosten
gewinn = (selbstkostenpreis / 100) * 20
barverkaufspreis = selbstkostenpreis + gewinn
verkaufsskonto = (barverkaufspreis / 98) * 2
zielverkaufspreis = barverkaufspreis + verkaufsskonto
verkaufsrabatt = (zielverkaufspreis / 95) * 5
listenverkaufspreisNetto = zielverkaufspreis + verkaufsrabatt
umsatzsteuer = listenverkaufspreisNetto * 0.19
listenverkaufspreisBrutto = umsatzsteuer+listenverkaufspreisNetto


# Ausgabe
print(listenverkaufspreisBrutto)
