##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random
import os

data = pandas.read_csv("birthdays.csv")
data_list = data.to_dict("records")

email = "fatihharsx4@gmail.com"
password = os.environ["password"]

def send_mail(e_mail, text):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=e_mail,
                            msg=f"Subject:Happy Birthday!\n\n{text}")

now = dt.datetime.now()
month = now.month
day = now.day

for i in data_list:
    if i["month"] == month and i["day"] == day:
        letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
        name = i["name"]
        e_mail = i["email"]
        with open(letter) as file:
            data = file.read()
        data = data.replace("[NAME]", name)

        send_mail(e_mail, text=data)



