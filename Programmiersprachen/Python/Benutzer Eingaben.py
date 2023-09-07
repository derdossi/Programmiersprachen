
#! Standard Eingabe ist Stringtyp
#! Benutzereingabe in einer Variable speichern.
name = input("Was ist dein Name?: ")

# alter = input("Wie alt bist du?: ")
# alter = alter + 1 # Fehler da Mathe nicht mit Strings möglich ist

alter = int(input("Wie alt bist du?: "))  # ! Konvertierung mit type casting

alter = alter + 1  # ! Mathe nun möglich

# ! Konvertierung zu Float Datentyp
groeße = float(input("Wie groß bist du?: "))

print("Hallo "+name)
# print("Du bist " +alter+" Jahre alt") #! Fehler da Konvertierung nötig ist
print("Du bist " + str(alter)+" Jahre alt")
print("Du bist " + str(groeße)+" cm groß")  # ! Konvertierung zum String
