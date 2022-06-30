import turtle
from tkinter import *

window = Tk()

# naming the window/program
window.title('My GUI Program')

# window minimum size specified
window.minsize(width=500, height=300)
window.config(padx=100, pady=200) #giving more space around the program

# how to make button clicked action
# use turtle module

# def button_clicked():
#     print('I got clicked')
#     new_text = input.get()
#     my_label.config(text=new_text)

# creating a label - always centred
# my_label = Label(text='I am a Label', font=('Arial', 24, 'bold'))
# my_label.config(text='New Text')
# # my_label.pack() # this is impt as it will pack the label into the GUI
# # my_label.pack(side= 'bottom') # can do alignment - left, right, bottom, top, expand to fill up the entire space
# my_label.pack()

#Button

# button = Button(text='Click Me', command=button_clicked)
# button.pack()

# Entry

# input = Entry(width=10)
# print(input.get())
# input.pack()

# LAYOUTS
# pack puts all the widgets in the centre one under another by default.

# PLACE - precise positioning by using a value for X and Y
# my_label = Label(text='I am a Label', font=('Arial', 24, 'bold'))
# my_label.config(text='New Text')
# # my_label.pack() # this is impt as it will pack the label into the GUI
# # my_label.pack(side= 'bottom') # can do alignment - left, right, bottom, top, expand to fill up the entire space
# my_label.place(x=100, y=200)

# GRID - can be divided by rows and columns
my_label = Label(text='I am a Label', font=('Arial', 24, 'bold'))
my_label.config(text='New Text')
my_label.grid(column=0, row=0) # cannot use pack and grid in the same file.

button1 = Button(text='Click Me')
button1.grid(column=1, row=1)

button2 = Button(text='Click Me')
button2.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)
# this keeps the window on screen and must be on the end of the code
window.mainloop()