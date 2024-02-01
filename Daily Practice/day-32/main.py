import random
import smtplib
import datetime as dt

#
# my_email = "john.s.piotrowski@gmail.com"
# password = "mgqw gtcc fame vnjd"
# to_email = "Kristinlewis2012@gmail.com"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=to_email,
#                         msg="Subject: John's Python Course! \n\n Hi, this is me sending you an email from Python :)"
#                         )


#
# now = dt.datetime.now()
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1990, month=7, day=23, hour=19)
# print(date_of_birth)

### ------ Monday Motivation ------ ###

# Email setup
my_email = "john.s.piotrowski@gmail.com"
password = "mgqw gtcc fame vnjd"
to_email = "Kristinlewis2012@gmail.com"

# Date setup
now = dt.datetime.now()
day_of_week = now.weekday()

#
if day_of_week == 0:
    with open("quotes.txt", "r", encoding="utf8") as file:
        all_quotes = file.readlines()
        random_quote = random.choice(all_quotes)
        print(random_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Monday Motivation! \n\n {random_quote}".encode("utf8")
        )
