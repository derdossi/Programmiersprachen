
#! Loops innerhalb einer anderen Loop. Die "innere" Loop beendet all ihre Wiederholungen
#! bevor die "äußere" Loop eine Wiederholung durchführt.

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
