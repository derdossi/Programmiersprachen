# Import Required Library
from tkinter import *
from tkcalendar import Calendar
import datetime as dt
# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

date = dt.datetime.today()
# Add Calendar
cal = Calendar(root, selectmode='day',
               year=date.year, month=date.month,
               day=date.day)

cal.pack(pady=20)


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())


datum_auswahl = cal.get_date()
diff = date-datum_auswahl


def grad_diff():
    date.config(text="Die Differenz lautet: " +
                diff)


# Add Button and Label
Button(root, text="Get Date",
       command=grad_date).pack(pady=20)

Button(root, text="Subtrahieren",
       command=grad_diff).pack(pady=20)

date = Label(root, text="")
date.pack(pady=20)

# Execute Tkinter
root.mainloop()
