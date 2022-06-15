"""
Function to implement email send using thread to reduce the email sending time. 
"""
from __future__ import annotations
import threading
from typing import TYPE_CHECKING

from mail import SendEmail

# To avoid cyclic import error
if TYPE_CHECKING:
    from user import User


class EmailThread(threading.Thread):
    def __init__(self, send_email: SendEmail, user: User) -> None:
        self.email = send_email
        self.user = user
        threading.Thread.__init__(self)

    def run(self) -> None:
        self.email.send(self.user)
