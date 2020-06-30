import smtplib
from email.message import EmailMessage
import socket


email = EmailMessage()

email['from'] = 'Prabhleen'
email['to'] = 'sainimanmeet9@gamil.com'
email['subject'] = 'sent using python'

email.set_content('Wowo this actually works!!!!!!!!!!!!!!!')

with smtplib.SMTP(host = 'smtp.gmail.com',port = 587) as smtp:
	socket.getaddrinfo('localhost', 25)
	smtp.ehlo()
	smtp.starttls()
	smtp.login('prabhleensaini14@gmail.com','Prabhu@13')
	smtp.send_message(email)