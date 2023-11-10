
#!   Loop Kontrolle =    Die Ausführung des Loops beeinflussen

#!   break =         benutzt um die Schleife komplett zu beenden
#!   continue =      überspringt zur nächsten Wiederholung
#!   pass =          macht nichts, wir als Platzhalter genutzt

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# Bindestriche aus einer Telefonnummer entfernen
# phone_number = "123-456-7890"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")        #! probier mit und ohne end="" um den unterschied zu sehen

# Nummern aufzählen ohne 13

for i in range(1, 21+1):  # ! +1 um auch bis 21 zu zählen
    if i == 13:
        pass
    else:
        print(i)
