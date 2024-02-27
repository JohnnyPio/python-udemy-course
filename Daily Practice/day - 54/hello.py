import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://media.giphy.com/media/'
            'v1.Y2lkPTc5MGI3NjExNWw4dmdyZGk5ZTBqYjF2MGx0bm1jNzJ4NG9oa3RhM3h6NWlwajR2cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UB9x43ZH3105v70743/giphy.gif">')


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def say_bye():
    return "Bye"


# Creating variable paths and converting the path
@app.route("/<name>/1")
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)
