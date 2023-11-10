name = "Azubi Speira"

print(len(name))  # ! Länge des names anzeigen lassen
print(name.find("A"))  # ! Den Index von A suchen im String - Index startet bei 0
# ! Den ersten Buchstaben im ersten Wort groß schreiben
print(name.capitalize())
print(name.upper())  # ! Alles groß schreiben
print(name.lower())  # ! Alles klein schreiben
print(name.isdigit())  # ! Ist der String eine Nummer? Gibt True oder False wieder
#! Besteht der String nur aus alphanumerischen Zeichen? - Hier False da leerzeichen
print(name.isalpha())
#! Wie viele bestimmte Buchstaben sind in dem String? - Hier 2
print(name.count("i"))
print(name.replace("i", "z"))  # ! Ersetzt i miz z im String
print(name*3)  # ! Die variable drei mal anzeigen lassen
