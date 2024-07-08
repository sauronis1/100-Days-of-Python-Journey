from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10)) ]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    # print(f"Your password is: {password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def get_data():

    data_website = website_entry.get()
    data_email = email_entry.get()
    data_password = password_entry.get()

    if data_website == "" or data_password == "":
        messagebox.showwarning(title="Error", message="Do not leave any of the fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=data_website, message=f"These are the details entered:\nEmail: "
                                                           f"{data_email}\nPassword: {data_password}\n"
                                                           f"Is it OK to save?")

        if is_ok:
            data_line = f"{data_website} | {data_email} | {data_password}\n"

            with open("data.txt", "a") as data_file:
                data_file.write(data_line)
                password_entry.delete(0, END)
                website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.configure(padx=40, pady=40)
window.title("Password Manager")

# Logo canvas
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(END, "user@email.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="ew")

add_button = Button(text="Add", width=36, command=get_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")


window.mainloop()
