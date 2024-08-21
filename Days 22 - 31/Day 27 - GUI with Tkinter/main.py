import tkinter


def button_clicked():
    new_text = input.get()
    label.config(text=new_text)

#window

window = tkinter.Tk()
window.title("Arnold smrdí")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

#label

label = tkinter.Label(text="fakt hodně", font=("Arial", 24, "bold"))
#label.place(x=100,y=200) #place layout manager - sucks because too specific ):
label.config(text="hodně")
label.grid(column=0, row=0)
label.config(padx=20, pady=20)

#button

button = tkinter.Button(text="Řekni Arnoldovi že smrdí", command=button_clicked)
button.grid(column = 1, row = 1)

button2 = tkinter.Button(text="click me", command=button_clicked)
button2.grid(column = 2, row = 0)

#Entry

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)
input.get()




window.mainloop() #has to be at the end of the program
