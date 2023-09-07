import time  # Zeit im code benutzen
#! Wird den Code block für eine limitierte Anzahl ausführen
#!
#!
#!           while loop = unlimitiert
#!           for loop = limitiert


# for i in range(10)
#    print(i)        #0-9
#    print(i+1)      #1-10

# for i in range(50,100):
#    print(i)        #!50-99

# for i in range(50,100+1): #!50-100, 51 Wiederholungen
#    print(i)

# for i in range(50,100+1,2)
#    print(i)        #!50-100, nur jede zweite Zahl

# for i in "Azubi Speira":
#    print(i)        #!Alle Buchstaben untereinander angezeigt


# countdown
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
