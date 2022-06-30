import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif' # creating an image for turtle to use. only .gif compatible with turtle
screen.addshape(image) # add image into the screen

turtle.shape(image) # change the shape of turtle to image so that image will display

data = pandas.read_csv('50_states.csv')
guessed_states = []


while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed",
                                    prompt="What's another state's name? ").capitalize()
    # print(answer_state)


    # need to check if answer_state is 1 of the state in the states column of 50_states.csv
        # if they got it right:
            # create a turtle to write the name of the state in the x and y coordinates on the map


    all_states = data.state.to_list()

    if answer_state == 'exit'.capitalize():
        missed_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        # print(missed_states)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv('states_to_learn.csv')
        break
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# states_to_learn.csv
