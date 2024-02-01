import datetime
import os
import pandas as pd
import random
import smtplib
import datetime as dt

##################### Extra Hard Starting Project ######################
# Constants
birthdays = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
letter_temp_dir = "./letter_templates/"
letter_templates = os.listdir(letter_temp_dir)
email_body = ""

# Current month and day
this_month = now.date().month
this_day = now.date().day

# 2. Check if today matches a birthday in the birthdays.csv
birthday_person = birthdays[(birthdays["month"] == this_month) & (birthdays["day"] == this_day)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if not birthday_person.empty:
    birthday_name = str(birthday_person.get("name").item())
    random_letter_template = random.choice(letter_templates)
    path = letter_temp_dir + random_letter_template
    with open(path, "r") as file:
        file_data = file.read()
        file_data.replace("[NAME]", "testy")
        file_data.replace("Angela", "John")
        email_body = file_data

print(email_body)

# 4. Send the letter generated in step 3 to that person's email address.
