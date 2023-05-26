import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()
import time


def sendMail(toEmail,subject,message):
    user=os.getenv('USER_EMAIL')
    password=os.getenv('USER_APP_PASSWORD')
    msg=MIMEMultipart()
    msg.set_unixfrom("Manas Gupta")
    msg['From']=user
    msg['To']=toEmail
    msg['Subject']=subject
    msg.attach(MIMEText(message))
    mailserver=smtplib.SMTP_SSL('smtp.gmail.com',465)
    mailserver.login(user,password)
    mailserver.sendmail(user,toEmail,msg.as_string())
    mailserver.quit()

if __name__=='__main__':
    email_list=[]
    mail=os.getenv('TO_EMAIL')
    for i in range(0,4):
        email_list.append(mail)

    for email in email_list:
        subject="Testing 1 2 3 .."
        message="Hi How are you"
        sendMail(email,subject,message)
        print(f"Email sent to {email}")
    print('All Mails sent sucessfully')