from tkinter import *


def calculate():
    miles = float(entry.get())
    km = round(miles * 1,609)
    result_label.config(text=f"{km}")


# Window
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=200, height=100)
window.configure(padx=20, pady=20)

# All the annoying labels
entry = Entry(width=10)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
