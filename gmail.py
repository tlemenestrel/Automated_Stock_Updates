import smtplib
import datetime
from email.mime.multipart import MIMEMultipart

class Gmail:

    def __init__(self):
        return

    def send_email(self,body):

        try:
            # Gmail account authentification

            gmail_user = 'tlemenestrel.stocks@gmail.com'
            gmail_password = 'tgcggazwusbnzwxa'

            # Set email configuration

            msg = MIMEMultipart('alternative')
            msg.attach(body)
            msg['From'] = 'tlemenestrel.stocks@gmail.com'
            msg['To'] = 'tlemenestrel.stocks@gmail.com'
            now = datetime.datetime.now()
            msg['Subject'] =  str(now.day) + '-' + str(now.month)  + '-' + str(now.year) + ' - ' + 'Stock Insights'

            # Send email

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail_user, gmail_password)

            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.close()

        except Exception as e:

            # Print thrown error

            print ("Error in the Gmail class: " + str(e))