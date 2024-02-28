from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0, 9)


def make_h1(func):
    def wrapper():
        return "<b>" + func() + "</b>"

    return wrapper


@app.route("/")
@make_h1
def game_start():
    return ("Guess a number between 0 and 9<br>"
            "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>")


@app.route("/<int:guessed_num>")
def game_on(guessed_num):
    if guessed_num > random_num:
        return ("<h1 style=color:red>Too high, try again!</h1>"
                "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif")
    elif guessed_num < random_num:
        return ("<h1 style=color:blue>Too low, try again!</h1>"
                "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif")
    else:
        return ("<h1 style=color:green>You found me!</h1>"
                "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif")


if __name__ == "__main__":
    app.run(debug=True)
