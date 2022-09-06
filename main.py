import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")
to_adr = os.getenv("TO_ADR")

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_adr,
                        msg="Subject:Hello\n\nThis is the body of my email")
