"""
Functions for sending email using smtplib
"""

import os
import smtplib

from dotenv import load_dotenv

load_dotenv()


class SendEmail:
    def __init__(self) -> None:
        """Setting SMTP Mail Server"""

        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(os.getenv("FROM_EMAIL"), os.getenv("EMAIL_PASSWORD"))

    def send(self, user) -> None:
        """SMTP Mail sending when user is registered."""

        SUBJECT = "Registration in Insight Workshop"
        TEXT = f"""
        Hi {user.email},
            You have successfully registered in Insight Workshop. 
        """
        message = "Subject: {}\n\n{}".format(SUBJECT, TEXT)
        self.server.sendmail(os.getenv("FROM_EMAIL"), user.email, msg=message)
