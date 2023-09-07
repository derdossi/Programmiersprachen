
#! Ein Codeblock der immer ausgeführt wird solange die Kondition Wahr ist

# while 1==1:
# print("Help! I'm stuck in a loop!") #! unendliche Schleife

# name = ""

# while len(name) == 0:
# name = input("Enter your name: ") #! user wird gelooped solange er keinen namen eingibt!


name = None

while not name:
    name = input("Enter your name:")

print("Hello "+name)
