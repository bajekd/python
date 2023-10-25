import os, smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


class Message:
    def __init__(self, receivers, subject):
        self.message = EmailMessage()
        self.message['From'] = EMAIL_ADDRESS

        self.message['To'] = receivers
        self.message['Subject'] = subject
        self.message.set_content(open('msg.txt').read())

        with open('merged_result.pdf', 'rb') as file:
            attachment_data = file.read()
            attachment_name = file.name
            self.message.add_attachment(attachment_data, maintype='application', subtype='octet-stream',
                                        filename=attachment_name)

    def send_mail(self):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(self.message)







