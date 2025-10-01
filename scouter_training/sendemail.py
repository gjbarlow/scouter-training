import smtplib
from email.message import EmailMessage

class SendEmail:
	def __init__(self, user="gregoryjbarlow@gmail.com", password="pjvb zwrv puru wkxs"):
		self.user = user
		self.password = password
		self.smtp_server = "smtp.gmail.com"
		self.smtp_port = 587

	def send(self, addr, subject, body):
		msg = EmailMessage()
		msg.set_content(body)
		msg['Subject'] = subject
		msg['From'] = self.user
		msg['To'] = addr

		with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
			server.starttls()
			server.login(self.user, self.password)
			server.send_message(msg)