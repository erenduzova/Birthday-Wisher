import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv

load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")
TO_ADR = os.getenv("TO_ADR")


def select_quote():
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
    return random.choice(all_quotes)


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    quote = select_quote()
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_ADR,
                            msg=f"Subject:Monday Motivation\n\n{quote}")
else:
    print("No")

