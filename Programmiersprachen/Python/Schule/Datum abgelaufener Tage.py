import datetime
today = datetime.date.today()
someday = datetime.date(2023, 1, 1)
diff = today - someday
diff.days
print(diff)
