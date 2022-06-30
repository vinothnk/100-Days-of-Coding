import tkinter

window = tkinter.Tk()

# naming the window/program
window.title('My GUI Program')

# window minimum size specified
window.minsize(width=500, height=300)

# creating a label - always centred
my_label = tkinter.Label(text='I am a Label', font=('Arial', 24, 'bold'))
# my_label.pack() # this is impt as it will pack the label into the GUI
# my_label.pack(side= 'bottom') # can do alignment - left, right, bottom, top, expand to fill up the entire space
my_label.pack(side='left')

my_label['text'] = 'New Text'
my_label.config(text='New Text')

#Button

button = tkinter.Button






# this keeps the window on screen and must be on the end of the code
window.mainloop()