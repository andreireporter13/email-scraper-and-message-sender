#
#
# This script will send a message to scraped emails
#
#
# import data: login, password etc.
from .config import email, password
#
from .text_data import plain_text, html_template
#
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#
class SendEmailTo:

    'This class is a blueprint for sending a message to some email adress.'

    

    def __init__(self, receiver_email: str, choose: int, message_subject: str):
        
        # email with data from user_input
        # ------------------------------> IMPORTANT <--------------------------
        #
        self.receiver_email = receiver_email.strip()    # email to send
        self.choose = choose                            # choose html_template or plain_text
        self.message_subject = message_subject.strip()  # message subject

        # default variables
        self.sender_email = email       # my default mail
        self.email_password = password  # email password

         # set emails 
        self.message = MIMEMultipart()
        self.message["Subject"] = self.message_subject
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email


        # make a choose in __init__ constructor
        if self.choose == 1:
            self.message.attach(MIMEText(plain_text, "plain"))
        
        elif self.choose == 2: 
            self.message.attach(MIMEText(html_template, "html"))
                

    # method for sending message 
    #
    def send_email_message(self):
        #
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, self.email_password)
            server.sendmail(
                self.sender_email, self.receiver_email, self.message.as_string()
        )


