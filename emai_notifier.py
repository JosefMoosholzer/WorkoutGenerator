from notion_api import get_exercises
from random import sample
from workout import Workout
from email.message import EmailMessage
import ssl, smtplib

def workout_str():
    return Workout(sample(get_exercises("core"), 5), 1).to_str()

sender_email_address = "seppitom@gmail.com"
sender_email_password = "hcwodrtjwkrnpzbe"
recipient_email_address = "jamoosholzer@hotmail.de"

subject = "Today's workout regime!"
body = workout_str()

em = EmailMessage()
em["From"] = sender_email_address
em["To"] = recipient_email_address
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port=465, context=context) as smtp:
    smtp.login(sender_email_address, sender_email_password)
    smtp.sendmail(sender_email_address, recipient_email_address, em.as_string())