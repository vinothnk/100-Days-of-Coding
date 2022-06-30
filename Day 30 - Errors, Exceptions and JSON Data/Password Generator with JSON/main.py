import random
from tkinter import messagebox
import pyperclip
import json

WHITE = '#FFFFFF'
BLACK = '000000'
FONT_NAME = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for char in range(nr_letters)]
    numbers_list = [random.choice(numbers) for char in range(nr_numbers)]
    symbols_list = [random.choice(symbols) for char in range(nr_symbols)]

    password_list = letters_list + numbers_list + symbols_list
    random.shuffle(password_list)
    # print(password_list)

    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_response = website_input.get()
    email_username_response = email_username_input.get()
    password_response = password_input.get()

    new_data = {
        website_response: {
            "email": email_username_response,
            "password": password_response,
        }
    }

    if len(website_response) == 0 or len(password_response) == 0:
        messagebox.showerror(title='Oops', message='Please do not leave any fields empty.')
    else:
        # is_ok = messagebox.askokcancel(title=website_response,
        #                            message=f'These are the details entered.\nEmail: {email_username_response}\n'
        #                                    f'Password: {password_response}\nIs it ok to save?')
        # assume user is ok with website and password

        # with open('data.json', mode='w') as data_file:  # changed data.txt to data.json. mode is w for write
        #     json.dump(new_data, data_file, indent=4) # to write into json files
        #     data = json.load(data_file) # to read the json file. must change mode to r
        #     print(data)

        # FOR UPDATING JSON FILE.
        # 1. change mode to w again.
        try:
            with open('data.json', mode='r') as data_file:
                # 2. load the data 1st
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # 3. update the data
            data.update(new_data)
            # 4. write back the data into the json file
            with open('data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()
    return


def search():
    try:
        with open('data.json', mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found')
    else:
        website_search = website_input.get()
        if website_search in data:
            messagebox.showinfo(title=website_search, message=f"Email:{data[website_search]['email']}\n"
                                                              f"Password: {data[website_search]['password']}")
        else:
            messagebox.showerror(title='Error', message='No Data Found')


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

# ADDING IMAGE to the canvas - DONE
window = Tk()
window.title('Password Manager App')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(125, 125, image=lock_img)
canvas.grid(row=0, column=1, padx=20, pady=20)

# Website/Email/Username/Password -> Labels
# Empty Textboxes -> Entries
# Generate/Add -> Buttons


# Website Label
website = Label(text='Website:')
website.grid(row=1, column=0)
# Website Entry
website_input = Entry(width=40)
website_input.grid(row=1, column=1)
website_input.focus()  # put cursor in the app when program start

# Email/Username Label
email_username = Label(text='Email/Username:')
email_username.grid(row=2, column=0)
# Email/Username Entry
email_username_input = Entry(width=40)
email_username_input.grid(row=2, column=1)
email_username_input.insert(0, 'wooo_hoooo07@hotmail.com')

# Password Label
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
# Password Entry
password_input = Entry(width=40)
password_input.grid(row=3, column=1)
# Generate Password Button
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2)

# Add Button
add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=0, columnspan=3)

# Search Button
search_button = Button(text='Search', width=10, command=search)
search_button.grid(row=1, column=2)
window.mainloop()
