import csv
import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_text = turtle.Turtle()
        state_text.hideturtle()
        state_text.penup()
        state_data = data[data.state == answer_state]
        state_text.goto(int(state_data.x), int(state_data.y))
        state_text.write(answer_state, align="center")

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break



