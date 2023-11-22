# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from tkcalendar import DateEntry
import datetime as dt
# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

date = dt.date.today

# Add Calendar
cal = Calendar(root, selectmode='day',
               year=date.year, month=date.month,
               day=date.day, date_pattern="ddmmy")

cal.pack(pady=20)


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())


# datum_auswahl = int(cal.get_date())
date_fix = date.strftime("%d%m%Y")
date_fix2 = int(date_fix)
# print(date_fix2)
# datum_auswahl = int(cal.get_date())
datum_auswahl = int(DateEntry())
diff = date_fix2-datum_auswahl


def grad_diff():
    date.config(text="Die Differenz lautet: " + str(diff))


# Add Button and Label
Button(root, text="Get Date",
       command=grad_date).pack(pady=20)

Button(root, text="Subtrahieren",
       command=grad_diff).pack(pady=20)

date = Label(root, text="")
date.pack(pady=20)

# Execute Tkinter
root.mainloop()

# print(cal.get_date())
# print(date_fix2)
# print(diff)
