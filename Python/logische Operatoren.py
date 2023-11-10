# and, or , not = Konditionen überprüfen

temp = int(input("Was ist die Temperatur draussen?: "))

if temp >= 0 and temp <=30:
    print("Schönes Wetter!")
    print("geh raus!")
elif temp < 0 or temp > 30:
    print("Schlechtes Wetter!")
    print("Bleib zuhause")

#if not(temp >= 0 and temp <=30):       umgekehrte Konditionen
    #print("Schlechtes Wetter!")
    #print("Bleib zuhause"
#elif not(temp < 0 or temp > 30):
    #print("Schönes Wetter!")
    #print("geh raus!" 
