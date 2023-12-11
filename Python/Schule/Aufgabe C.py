# Aufgabe C

kapital = 10000
p=.02
j=0

while(kapital < 20000):
    zinsen = (kapital/100) * p
    kapital = kapital + zinsen
    j= j+1
print(kapital)
print("die Laufzeit beträgt : "+ str(j))
