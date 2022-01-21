from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
smtphost = "email-smtp.us-east-1.amazonaws.com"
# Get the user name and password - from the IAM user that is created by SES.
password = "BHPwFenCeDAVG/ceWCcRauM/nNlX07rDxrGa/ZecPvgC"
username = "AKIA4AUWBYEHKXXTGRGM"
message = "Test from Python via AuthSMTP"
msg = MIMEMultipart()
msg['From'] = "jigyasabot@tmlbsl.com"
msg['To'] = "debanjanchakraborty@yahoo.co.in"
msg['Subject'] = "Test from Python via AuthSMTP"
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP(smtphost)
server.starttls()
server.login(username, password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()