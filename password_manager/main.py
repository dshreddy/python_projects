# Author : Sai Hemanth Reddy
# Date : 16 april 2023

import json
import random
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen():
    entry_3.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    entry_3.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_1.get()
    mail = entry_2.get()
    pw = entry_3.get()
    new_data = {
        website: {
            "email": mail,
            "password": pw
        }
    }

    if len(website) == 0 or len(mail) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure there are no empty fields")
    else:
        ans = messagebox.askokcancel(title=f"{website}", message="Confirm saving the entered details ?")
        if ans:
            try:
                with open("pass_words.json", 'r') as file:
                    data = json.load(file)
            except:
                with open("pass_words.json", 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                # updating old data with new data
                data.update(new_data)

                with open("pass_words.json", 'w') as file:
                    # Saving the updated data
                    json.dump(data, file, indent=4)
            finally:
                entry_1.delete(0, END)
                entry_2.delete(0, END)
                entry_2.insert(0, "112101014@smail.iitpkd.ac.in")
                entry_3.delete(0, END)
        else:
            entry_1.delete(0, END)
            entry_2.delete(0, END)
            entry_2.insert(0, "112101014@smail.iitpkd.ac.in")
            entry_3.delete(0, END)

#---------------------------- FIND PASS WORD ------------------------------- #
def find_pw():
    website = entry_1.get()

    try:
        with open("pass_words.json") as file:
            data = json.load(file)
    except:
        messagebox.showinfo(title=website, message="No data file found\n")
    else:
        with open("pass_words.json") as file:
            data = json.load(file)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"User name : {email}\n Password : {password}\n")
            else:
                messagebox.showinfo(title=website, message="No details found for the entered website\n")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(500, 500)
window.config(pady=50, padx=100)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

label_1 = Label(text="Website")
label_1.grid(row=1, column=0, )

label_2 = Label(text="Email/ Username")
label_2.grid(row=2, column=0)

label_3 = Label(text="Password")
label_3.grid(row=3, column=0)

entry_1 = Entry(width=21)
entry_1.grid(row=1, column=1)

entry_2 = Entry(width=38)
entry_2.insert(0, "112101014@smail.iitpkd.ac.in")
entry_2.grid(row=2, column=1, columnspan=2)

entry_3 = Entry(width=21)
entry_3.grid(row=3, column=1)

btn_1 = Button(text="Generate Password", command=gen)
btn_1.grid(row=3, column=2)

btn_2 = Button(text="Add", width=36, command=save)
btn_2.grid(row=4, column=1, columnspan=2)

btn_3 = Button(window, text="Search", bg="#0000FF", fg="BLACK", command=find_pw)
btn_3.grid(row=1, column=2)

window.mainloop()
