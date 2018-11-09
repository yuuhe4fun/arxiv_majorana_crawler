import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open('Adress_list.txt', 'r') as f:
    toAddress = [line.strip() for line in f]
fromaddr = "Majorana.Arxiv@gmail.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = 'Topo'

msg['Subject'] = "Python testing email"

body = '''Dear topo,
This is a test mail using MIME. Seems to work well.
This is the body of the mail.

Regards,
Majorana.Arxiv

'''

msg.attach(MIMEText(body, 'plain'))
Message = msg.as_string()

try:
    conn = smtplib.SMTP('smtp.gmail.com', 587) #smtp address and port
    conn.ehlo() #call this to start the connection
    conn.starttls() #starts tls encryption. When we send our password it will be encrypted.
    conn.login('Majorana.Arxiv@gmail.com', 'Braiding2019')
    conn.sendmail('Majorana_Arxiv@gmail.com', toAddress, Message)
    conn.quit()
    print('Sent notificaton e-mails for the following recipients:\n')
    for i in range(len(toAddress)):
        print(toAddress[i])
except smtplib.SMTPException:
    print('Error: Failed to send mail.')
    
