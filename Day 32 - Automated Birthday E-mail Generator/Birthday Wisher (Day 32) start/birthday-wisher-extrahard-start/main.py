##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import smtplib
import random


### birthday ordinals ###
SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}


def get_ordinal(i):
    # Adapted from https://codereview.stackexchange.com/questions/41298/producing-ordinal-numbers
    if 10 <= i % 100 <= 20:
        return 'th'
    else:
        return SUFFIXES.get(i % 10, 'th')


# Check if today matches a birthday in the birthdays.csv
today_date = dt.date.today()
birthday_data = pd.read_csv("./birthdays.csv")
birthday_boys = birthday_data.loc[(birthday_data["month"] == today_date.month)
                                  & (birthday_data["day"] == today_date.day)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv
if birthday_boys.empty:
    print("No birthday wishes today, boss!")
else:
    for index, birthday_boy in birthday_boys.iterrows():
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter:
            letter_text = letter.read()

        # Replacing the name
        new_name = birthday_boy["name"]
        letter_text = letter_text.replace("[NAME]", new_name)

        # Replacing the age
        friends_age = today_date.year - birthday_boy["year"]
        birthday_ordinal = get_ordinal(friends_age)
        xth_birthday = f"{friends_age}{birthday_ordinal}"
        letter_text = letter_text.replace("[X]", xth_birthday)

        # 4. Send the letter generated in step 3 to that person's email address.
        my_email = ""
        password = ""
        friends_email = birthday_boy["email"]

        with smtplib.SMTP("smtp.forpsi.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                           to_addrs=friends_email,
                          msg=f"From: Your good friend\nSubject:Birthday Wish\n\n{letter_text}")
