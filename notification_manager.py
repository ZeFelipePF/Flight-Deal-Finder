import os
from twilio.rest import Client

class NotificationManager:
    
    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ['TWILIO_TOKEN'])

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_NUMBER"],
            body=message_body,
            to=os.environ["MY_PHONE_NUMBER"]
        )
        print(message.sid)