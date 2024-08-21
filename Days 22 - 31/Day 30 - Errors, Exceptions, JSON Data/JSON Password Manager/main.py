from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
        new_data = {
            data_website: {
                "E-mail": data_email,
                "Password": data_password,
            }
        }
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                data.update(new_data)
                json.dump(data, data_file, indent=4)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)

# ---------------------------- FIND PASSWORD -------------------------- #


def find_password():
    key_website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            pyperclip.copy(data[key_website]["Password"])
            messagebox.showinfo(title=key_website, message=f"E-mail: {data[key_website]["E-mail"]}"
                                                           f"\nPassword: {data[key_website]["Password"]}")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data found - try saving some passwords first.")
    except KeyError as key_error:
        messagebox.showwarning(title="Error", message=f"No entry found for '{key_error}'.")


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
website_entry.grid(row=1, column=1, sticky="ew")
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

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="ew")

window.mainloop()
