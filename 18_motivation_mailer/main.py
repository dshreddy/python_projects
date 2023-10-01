import random
import smtplib
import datetime as dt

now = dt.datetime.now()

if now.weekday() > 0:

    with open("quotes.txt") as file:
        all_quotes = file.readlines()
    quote = random.choice(all_quotes)

    my_email = "dshreddy03@gmail.com"
    password = "oojnodyvgrslwjkq"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, to_addrs="112101014@smail.iitpkd.ac.in",
            msg=f"Subject : Monday Motivation    \n\n{quote}"
        )