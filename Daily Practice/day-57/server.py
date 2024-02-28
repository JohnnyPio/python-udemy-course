from flask import Flask, render_template
import datetime
import random

app = Flask(__name__)

my_name = "Johnny Pio"
current_year = datetime.date.today().year
print(current_year)


@app.route("/")
def home():
    rand_num = random.randint(1, 10)
    return render_template("index.html", my_rand_num=rand_num, MY_NAME=my_name, CURRENT_YEAR=current_year)


if __name__ == "__main__":
    app.run(debug=True)
