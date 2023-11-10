
#!  tuple = Kollektion die nicht verändert werden kann. (Wie liste nur unveränderbar)
#!      benutzt um relevante Daten zu gruppieren

student = ("Azubi", 21, "Maennlich")

print(student.count("Azubi"))
print(student.index("Maennlich"))

for x in student:
    print(x)

if "Azubi" in student:
    print("Azubi ist hier")
