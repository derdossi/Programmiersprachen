
#! Wörterbuch = Eine änderbare, ungeordnete Sammlung von einzigartigen key:value Paaren.
#!              Schnell da sie hashing benutzen. Zugang zu einem Wert erfolgt schnell

capitals = {'USA': 'Washington DC',
            'India': 'NewDelhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}


# print(capitals['Germany'])  #!Schlechte Vorgehensweise da Fehler bei nicht existenten Werten
# print(capitals.get('Germany')) #! Keine Fehler sondern None
# print(capitals.keys()) #! Nur die keys anzeigen lassen
# print(capitals.values()) #! Nur die values anzeigen lassen
# print(capitals.items()) #! Alle Werte anzeigen lassen

# capitals.update({'Germany': 'Berlin'})  # ! Neuen key:value einfügen
# capitals.update({'USA': 'Las Vegas'})  # ! Vorhandenen key verändern
# capitals.pop('China')  # ! Kompletten key:value löschen
# capitals.clear()  # ! Komplettes Wörterbuch löschen

for key, value in capitals.items():  # ! Schönere Ansicht der Daten
    print(key, value)
