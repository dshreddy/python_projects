import requests
from bs4 import BeautifulSoup
import smtplib
import os

affordable_price = 1600

url = "https://www.amazon.in/Adidas-Synthetic-Textile-Merage-Running/dp/B0B3JTJY5P/ref=sr_1_20?keywords=adidas+running+shoes&qid=1696345064&sr=8-20"
headers = {'Accept-Language' : "en-US,en;q=0.9",
            'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find(name="span", class_="a-offscreen").text[1:]
price = int(price.replace(',', ''))

MY_EMAIL = "dshreddy03@gmail.com"
MY_EMAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

if price < affordable_price:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
            msg=f"Subject : Price Drop    \n\n The price of item is now at Rs.{price}"
        )
