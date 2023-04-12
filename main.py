# """imported smtplib module"""
# import smtplib
#
# """variable to store email address and password"""
# myEmail = "gpython72@gmail.com"
# password = "blxfzquksftguoxk"
#
# """variable to store receiver's address"""
# receiver = "anshujuly26@yahoo.com"
#
# with smtplib.SMTP(
#     "smtp.gmail.com",
#     port=587,
#     timeout=25
# ) as connection:
#
#     """securing our connection"""
#     connection.starttls()
#
#     """login"""
#     connection.login(
#         user=myEmail,
#         password= password
#     )
#
#     """send mail"""
#     connection.sendmail(
#         from_addr=myEmail,
#         to_addrs=receiver,
#         msg="Subject:Hi!\n\nThis is the new body of the message."
#     )

# ------------------------------------------------------------

## working with the datetime module

# """imported datetime module as dt"""
# import datetime as dt
#
# """created now object"""
# now = dt.datetime.now()
#
# year = now.year
# month = now.month
# day = now.day
#
# date = now.date()
#
# dayOfTheWeek = now.weekday()
# print(dayOfTheWeek)
#
# dateOfBirth = dt.datetime(year=2003, month=7, day=26)
# print(dateOfBirth.date())

# ------------------------------------------------------------

## challenge 1: send motivational quotes on wednesday via email

"""imported smtplib module"""
import smtplib

"""imported datetime module as dt"""
import datetime as dt

"""imported random module"""
import random

"""created the now object"""
now = dt.datetime.now()
dayOfTheWeek = now.weekday()

"""variable to store email address and password"""
myEmail = "gpython72@gmail.com"
password = "blxfzquksftguoxk"

"""variable to store receiver's address"""
receiver = "anshujuly26@yahoo.com"

"""reading text file"""
with open("quotes.txt") as file:
    quotesList = file.readlines()

"""send email when it's wednesday"""
if dayOfTheWeek == 2:
    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=25) as connection:
        connection.starttls()
        connection.login(
            user=myEmail,
            password=password,
        )
        connection.sendmail(
            from_addr=myEmail,
            to_addrs=receiver,
            msg=f"Subject:Wednesday motivational quote!\n\n{random.choice(quotesList)}",
        )