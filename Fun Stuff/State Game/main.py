import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

num_states_guessed = 0
states_left = all_states

while num_states_guessed < 50:
    answer_state = screen.textinput(title=f"{num_states_guessed}/50 Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state in all_states:
        state_text = turtle.Turtle()
        state_text.hideturtle()
        state_text.penup()
        state_data = data[data.state == answer_state]
        state_text.goto(int(state_data.x), int(state_data.y))
        state_text.write(answer_state, align="center")

    # Error Handling if the same state is guessed again
    if answer_state in states_left:
        states_left.remove(answer_state)
        num_states_guessed += 1

turtle.mainloop()
