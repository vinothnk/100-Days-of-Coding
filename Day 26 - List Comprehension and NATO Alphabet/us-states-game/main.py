import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif' # creating an image for turtle to use. only .gif compatible with turtle
screen.addshape(image) # add image into the screen

turtle.shape(image) # change the shape of turtle to image so that image will display

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
data = pandas.read_csv('50_states.csv')
answer_list = []
counter = 0
guess = 0
answer_state = screen.textinput(title='Guess the state', prompt="What's another state's name? ").capitalize()
data.loc[data['state'] == answer_state] = answer_list.append(answer_state)

while counter != 50:
    answer_state = screen.textinput(title=f"{guess}/50 States Correct", prompt="What's another state's name? ").capitalize()
    # print(answer_state)
    data.loc[data['state'] == answer_state] = answer_list.append(answer_state)




    screen.exitonclick()

