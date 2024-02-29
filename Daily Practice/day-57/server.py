from flask import Flask, render_template
import datetime
import random
import requests

app = Flask(__name__)

my_name = "Johnny Pio"
current_year = datetime.date.today().year


@app.route("/")
def home():
    return "Hello world"
    # rand_num = random.randint(1, 10)
    # return render_template("index.html", my_rand_num=rand_num, MY_NAME=my_name, CURRENT_YEAR=current_year)


def get_gender(your_name):
    gender_request = requests.get(f"https://api.genderize.io?name={your_name}&country_id=US")
    gender = gender_request.json().get("gender")
    return gender


def get_age(your_age):
    age_request = requests.get(f"https://api.agify.io?name={your_age}&country_id=US")
    age = age_request.json().get("age")
    return age


@app.route("/guess/<name>")
def guessing(name):
    your_age = get_age(name)
    your_gender = get_gender(name)
    return render_template("index.html", YOUR_NAME=name, YOUR_GENDER=your_gender, YOUR_AGE=your_age)


if __name__ == "__main__":
    app.run(debug=True)
