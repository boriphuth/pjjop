import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from nameko.rpc import rpc

def send(id, firstname, lastname, email):
    msg = EmailMessage()
    text = "สวัสดีครับ คุณ " + firstname + " " + lastname + " รหัสนักศึกษา " + str(id) + " ได้ลงทะเบียนแล้ว"
    msg.set_content(text)

    msg['Subject'] = 'Register complete'
    msg['To'] = email

    s = smtplib.SMTP("smtp",25)
    s.ehlo()
    s.sendmail(from_addr = 'boriphuth.sa@gmail.com', to_addrs = email, msg = msg.as_string())
    s.quit()


class Email:
    name = "email"

    @rpc
    def send(self, id, firstname, lastname, email):
        send(id, firstname, lastname, email)