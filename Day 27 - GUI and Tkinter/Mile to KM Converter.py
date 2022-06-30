from tkinter import *

window = Tk()

# naming the window/program
window.title('Miles to KM Convertor')

# window minimum size specified
window.minsize(width=400, height=200)

empty_km = 0

def action():
    miles_to_km = float(value) * 1.609
    my_label4.update(miles_to_km)
    return



my_label1 = Label(font=('Arial', 14, 'bold'))
my_label1.config()
my_label1.grid(column=0, row=0) # cannot use pack and grid in the same file.

my_label2 = Label(text='is equal to',font=('Arial', 14, 'bold'))
my_label2.config(text='is equal to')
my_label2.grid(column=1, row=1) # cannot use pack and grid in the same file.



my_label3 = Label(text='Miles',font=('Arial', 14, 'bold'))
my_label3.config(text='Miles')
my_label3.grid(column=3, row=0) # cannot use pack and grid in the same file.

my_label4 = Label(text=empty_km,font=('Arial', 14, 'bold'))
my_label4.config(text=empty_km)
my_label4.grid(column=2, row=1) # cannot use pack and grid in the same file.

my_label3 = Label(text='KM',font=('Arial', 14, 'bold'))
my_label3.config(text='KM')
my_label3.grid(column=3, row=1) # cannot use pack and grid in the same file.

button = Button(text="Convert", command=action)
button.grid(column=2, row=2)
# this keeps the window on screen and must be on the end of the code
window.mainloop()