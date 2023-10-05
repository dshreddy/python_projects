import random
import pandas as pd
import datetime as dt
import smtplib
import os

# Using pandas to read the bday data
df = pd.read_csv('birthdays.csv')
df = df.to_dict()

# Checking the date and time when the programme is being runned
now = dt.datetime.now()
curr_month = now.month
curr_day = now.day

# A list to store (mail, name) of people having birthday on today
recipients_mails = []

for key in df['month']:
    if df['month'][key] == curr_month:
        if df['day'][key] == curr_day:
            recipients_mails.append((df['email'][key], df['name'][key]))

# Sending mails to persons having birthday's as today
for person in recipients_mails:

    # Choosing a random template to send mail
    letter = random.randint(1, 3)
    file_name = "letter_templates/"+"letter_"+str(letter)+".txt"

    # Opening letter and replacing [NAME] with actual name
    with open(file_name) as file:
        data = file.read()
        data = data.replace("[NAME]", person[1])

    # Sending the mail
    my_email = "dshreddy03@gmail.com"
    password = os.getenv("MAIL_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        # tls is for securing the connection
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, to_addrs=person[0],
            msg=f"Subject : Happy Birthday !\n\n{data}"
        )
        connection.close()

