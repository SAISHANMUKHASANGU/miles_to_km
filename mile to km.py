from tkinter import *

window=Tk()
window.minsize(width=300,height=200)
window.config(padx=100,pady=100)

input=Entry(width=10)
input.grid(row=0,column=1)

my_label=Label(text="is equal to")
my_label.config(padx=10,pady=10)
my_label.grid(row=1,column=0)

my_label_1=Label(text="km")
my_label_1.config(padx=10,pady=10)
my_label_1.grid(row=1,column=2)

my_label_2=Label(text="miles")
my_label_2.config(padx=10,pady=10)
my_label_2.grid(row=0,column=2)

my_label_3=Label(text="0")
my_label_3.config(padx=10,pady=10)
my_label_3.grid(row=1,column=1)

def calculate():
    km=float(input.get())*1.609
    my_label_3.config(text=f"{km}")

button=Button(text="Calculate",command=calculate)
button.grid(row=2,column=1)

window.mainloop()
