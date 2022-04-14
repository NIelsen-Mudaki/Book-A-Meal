# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
# import email
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail




print('ran email')

def send_email(recipients):
    message = Mail(
        from_email='bookamealtoday@gmail.com',
        to_emails=recipients,
        subject='Brasserie Menu',
        html_content='<strong>Our Menu is ready.Please head to our site and check it out</strong>',
        is_multiple=True
        
        )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

# send_email(['francizgithae@gmail.com','francis.githae@student.moringaschool.com'])