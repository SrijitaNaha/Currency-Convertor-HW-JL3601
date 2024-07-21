from tkinter import *
from tkinter import ttk
import math

def convert():
    rs_amt = rs_entry.get()
    dollar_amt = (float(rs_amt)/83)
    convert_lbl.config(text = str(round(dollar_amt)))


root = Tk()
root.title("Currency Convertor")

# Adding heading inside window
heading = Label(text="Currency Convertor(Rs -> $)",font=("Arial",20),fg="purple")
heading.pack()

frame = Frame(root)
frame.pack(pady=20)

# Entering currency in Rs
rs_lbl = Label(frame,text="Enter amount in Rs: ",font=("Arial",10))
rs_lbl.grid(row=0,column=0)
\
rs_entry = Entry(frame)
rs_entry.grid(row=0,column=1)

# Displaying amount in dollar
dollar_lbl = Label(frame,text="Amount in Dollar($): ",font=("Arial",10))
dollar_lbl.grid(row=1,column=0)

convert_lbl = Label(frame,font=("Arial",10))
convert_lbl.grid(row=1,column=1)

# Creating the convert button
convert_btn = Button(frame,text="Convert",font=("Arial",14),width=30,bg="navy blue",fg="white",command=convert)
convert_btn.grid(row=3, column=0, columnspan=2, pady=10)




root.mainloop()