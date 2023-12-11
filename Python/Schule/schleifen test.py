# Aufgabe A

kapital = 10000

p = .02  # in %

j = 0

while (j < 10):
    zinsen = (kapital / 100) * p
    kapital = kapital + zinsen
    j = j + 1
print(kapital)
