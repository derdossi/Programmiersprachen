import datetime
heute = datetime.date.today()
testdatum = datetime.date(2023, 1, 1)
diff = heute - testdatum
diff.days
print(diff)
