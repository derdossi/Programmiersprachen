
#! index operator [] = erlaubt Zugang zu Werten einer Reihenfolge (Strings, list, tuples)

# name = "Azubi Speira"

# if (name[0].islower()):         #! Wenn der erste Buchstabe kleine geschrieben ist
#     name = name.capitalize()    #! Ersten Buchstabe im String groß schreiben


# print(name)

name = "Azubi Speira!"

first_name = name[:5].upper()
last_name = name[6:].lower()
last_character = name[-1]


print(first_name)
print(last_name)
print(last_character)
