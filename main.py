"""imported smtplib module"""
import smtplib

"""variable to store email address and password"""
myEmail = "gpython72@gmail.com"
password = "blxfzquksftguoxk"

"""variable to store receiver's address"""
receiver = "anshujuly26@yahoo.com"

with smtplib.SMTP(
    "smtp.gmail.com",
    port=587,
    timeout=25
) as connection:

    """securing our connection"""
    connection.starttls()

    """login"""
    connection.login(
        user=myEmail,
        password= password
    )

    """send mail"""
    connection.sendmail(
        from_addr=myEmail,
        to_addrs=receiver,
        msg="Subject:Hi!\n\nThis is the new body of the message."
    )
