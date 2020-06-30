import smtplib
from email.message import EmailMessage
import socket
from string import Template
from pathlib import Path

html = Template(Path('dynamic_mail.html').read_text())

email = EmailMessage()

email['from'] = 'Prabhleen'
email['to'] = '18bcs134@ietdavv.edu.in'
email['subject'] = 'This is dynamic mail#2'

email.set_content(html.substitute({'name':'Prabhleen'}),'html')

with smtplib.SMTP(host = 'smtp.gmail.com',port = 587) as smtp:
	
	socket.getaddrinfo('localhost', 25)
	smtp.ehlo()
	smtp.starttls()
	smtp.login('prabhleensaini14@gmail.com','Prabhu@13')
	smtp.send_message(email)
	print('you\'re the boss')
