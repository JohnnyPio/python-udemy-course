import smtplib

my_email = "john.s.piotrowski@gmail.com"
password = "mgqw gtcc fame vnjd"
to_email = "northeastmanic1967@yahoo.com"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="hello, this is a test run.")
connection.close()
