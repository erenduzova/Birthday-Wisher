import smtplib
import datetime as dt
import os
from dotenv import load_dotenv
import random
import pandas as pd


load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")
TO_ADR = os.getenv("TO_ADR")

birthdays_data = pd.read_csv("birthdays.csv")
birt_dict = birthdays_data.to_dict(orient="records")

print(birt_dict)

# Get Today's Date
today = dt.datetime.now()
today_month = today.month
today_day = today.day


# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#     connection.sendmail(from_addr=MY_EMAIL,
#                         to_addrs=TO_ADR,
#                         msg=f"Subject:Monday Motivation\n\nletter")
