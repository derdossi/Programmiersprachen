
#! Funktionsaufrufe innerhalb andere Funktionsaufrufe.
#! Innerste Funktionsaufrufe werden zuerst aufgelöst
#! Der Wert wird manchmal also teil der äusseren Funktion benötigt

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))
