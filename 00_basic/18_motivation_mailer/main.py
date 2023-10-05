import random
import smtplib
import datetime as dt
import os

now = dt.datetime.now()

if now.weekday() > 0:

    with open("quotes.txt") as file:
        all_quotes = file.readlines()
    quote = random.choice(all_quotes)

    my_email = "SENDERS_MAIL"
    password = os.getenv("MAIL_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, to_addrs="RECEIVERS_MAIL",
            msg=f"Subject : Monday Motivation    \n\n{quote}"
        )