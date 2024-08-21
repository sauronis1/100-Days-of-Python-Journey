import smtplib

my_email = ""
password = ""

# now = dt.datetime.now()
# year = now.year
# print(now)

# date_of_birth = dt.datetime(year=1990, month=3, day=31, hour=16, minute=33)
# print(date_of_birth)

import datetime as dt
import random

today_date = dt.date.today()
day_of_week = today_date.isoweekday()
if day_of_week == 1:
    with open("quotes.txt", "r") as quotes:
        lines = [line.rstrip() for line in quotes]

    with smtplib.SMTP("smtp.forpsi.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                           to_addrs="",
                          msg=f"From: sauronis\nSubject:Motivational quote\n\n{random.choice(lines)}")