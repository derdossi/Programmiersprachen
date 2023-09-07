# if statement

age = int(input("Wie alt bist du?: "))


if age == 100:
    print("Du bist ein Jahrhundert alt")
elif age >= 18:
    print("Du bist Volljährig!")
# elif age == 100:
    # print("Du bist ein Jahrhundert alt")       Muss an den Anfang da sonst age = 100 "Du bist volljährig ergibt". Reihenfolge wichtig
elif age < 0:
    print("Du wurdest noch nicht geboren!")
else:
    print("Du bist nicht Volljährig!")
