# import smtplib
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

import datetime as dt

now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1990, month=7, day=23, hour=19)
print(date_of_birth)