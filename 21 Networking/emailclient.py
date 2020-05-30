import smtplib

from email.mime.text import MIMEText        # This is used to build our email message including body, subject

body = 'This is a Test of Email Automation'

msg = MIMEText(body)

msg['From'] = "senders_email_addres"
msg['To'] =  "receiver1_email_address, receiver2_email_address"
msg['Subject'] = "This is a Subject"

server = smtplib.SMTP('smtp.gmail.com',587)     # 587 is the global default port for this

server.starttls()

server.login("senders_email_address","senders_password")

server.send_message(msg)

print("Mail Sent")

server.quit()

'''Do "Allow Less Secure Apps" on 'myaccount.google.com' of sender's gmail account'''