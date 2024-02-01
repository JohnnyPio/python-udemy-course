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

my_email = "john.s.piotrowski@gmail.com"
password = "mgqw gtcc fame vnjd"
to_email = "Kristinlewis2012@gmail.com"

# Current month and day
this_month = now.date().month
this_day = now.date().day

# 2. Check if today matches a birthday in the birthdays.csv
birthday_person = birthdays[(birthdays["month"] == this_month) & (birthdays["day"] == this_day)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
if not birthday_person.empty:
    birthday_name = str(birthday_person.get("name").item())
    random_letter_template = random.choice(letter_templates)
    path = letter_temp_dir + random_letter_template
    with open(path, "r", encoding="utf8") as file:
        file_data = file.read()
        file_data = file_data.replace("[NAME]", birthday_name)
        file_data = file_data.replace("Angela", "John")

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Happy Birthday {birthday_name}! \n\n {file_data}".encode("utf8")
        )
