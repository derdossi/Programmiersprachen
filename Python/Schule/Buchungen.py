Buchungen = 140

Buchungen2 = float(Buchungen)

if Buchungen <= 50:
    kosten = Buchungen * 0.1 + 4
elif Buchungen <= 100:
    kosten = 50 * 0.1 + (Buchungen-50) * 0.08 + 4
elif Buchungen <= 150:
    kosten = 50 * 0.10 + 50 * 0.08 + (Buchungen-100) * 0.06 + 4

print(kosten)
