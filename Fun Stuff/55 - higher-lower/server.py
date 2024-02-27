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
        return f"Too high!"
    elif guessed_num < random_num:
        return f"Too low!"
    else:
        return f"Niiiice"


if __name__ == "__main__":
    app.run(debug=True)
