
#! Strings schneiden mit indexing []
#! [start:stop:step]
name = "Azubi Speira"

first_name = name[0:5]  # ? = first_name = name[:5]
last_name = name[6:12]  # ? =last_name = name [6:]
funky_name = name[::2]  # ! step. Nur jeder zweite Buchstabe wird gezählt.
reversed_name = name[::-1]  # ! Namen umdrehen

print(first_name)
print(last_name)

#! Strings schneiden mit slice()
#! (start,stop,step)
website1 = "http://google.com"
website2 = "http://wikipedia.com"

#! negative nummern fangen ganz hinten im string an. -4 schneidet ".com" weg
slice = slice(7, -4)

print(website1[slice])
print(website2[slice])
