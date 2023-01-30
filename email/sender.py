import smtplib 
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = ''
email['to'] = ''
email['subject'] = 'worked'

email.set_content(html.substitute({'name':'Brick'}), 'html')

with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('', '')
    smtp.send_message(email)
    print('Ok')