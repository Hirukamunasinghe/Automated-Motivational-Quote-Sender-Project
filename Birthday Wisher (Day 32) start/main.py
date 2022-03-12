from smtplib import SMTP
import datetime as dt
import random

MY_EMAIL ="hirukamunn@gmail.com"
PASSWORD="ABCD5678"

now = dt.datetime.now()
weekday = now.weekday()
if weekday ==0:
    with open("quotes.txt")as quote_file:
        all_quotes=quote_file.readlines()
        quote = random.choice((all_quotes))

    print(quote)
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="munasinghehiruka@gmail.com",msg =f"Subject:Monday Motivation"
                                                                                            f"\n\n{quote}")


# from smtplib import SMTP
#
# my_email ="hirukamunn@gmail.com"
# password = "ABCD5678"
#
# with SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="binadeemunasinghe@gmail.com",msg ="Subject:Hello\n\nThis is the body of"
#                                                                                        " my email")

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
#
# date_of_birth = dt.datetime(year=2005, month=8, day=15, )
# print(date_of_birth)


