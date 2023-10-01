from tkinter import *

window = Tk()
window.minsize(width=400, height=400)
window.config(padx=100, pady=100)

miles = Entry()
miles.grid(row=0, column=1)

label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)

label_2 = Label(text="is equal to")
label_2.grid(row=1, column=0)

label_3 = Label(text="------")
label_3.grid(row=1, column=1)

label_4 = Label(text="Km")
label_4.grid(row=1, column=2)


def calculate():
    mil = int(miles.get())
    km = 0.6214*mil
    label_3.config(text=f"{km}")


btn = Button(text="Calculate", command=calculate)
btn.grid(row=2, column=1)
window.mainloop()
