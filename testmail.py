import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "mahunta.poonam@gmail.com"
toaddr = "mahunta.poonam@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "CPF TEST"
 
body = "TESTING COMPLETE"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.valeo.com', 587)
server.starttls()
server.login(fromaddr, "bel12345")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
