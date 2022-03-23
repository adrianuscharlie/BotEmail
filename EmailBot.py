from email.message import EmailMessage
import os
import mimetypes
import smtplib
import getpass


def Message(sender, recepient,subject,path_txt):
    """Function to build the message"""
    file=open(path_txt)
    message=EmailMessage()
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recepient
    message['Subject'] = subject
    content=file.read()
    message.set_content(content)
    return message

def addAttachment(message,path):
    """Function to add attachment to the message"""
    mime_type, _ = mimetypes.guess_type(path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(path, 'rb') as file:
        message.add_attachment(file.read(), maintype=mime_type, subtype=mime_subtype,
                               filename=os.path.basename(path))
    return message

def sendEmail(message,password,server='smtp.gmail.com'):
    """Function to send email from sender to recipient"""
    mail_server = smtplib.SMTP_SSL(server, 465) #The 2nd parameter is the code of gmail server
    mail_server.login(message['From'], password)
    mail_server.send_message(message)
    mail_server.close()
def main():
    """Main function that you can edit followed by your condition"""
    message=Message("sender@gmail.com","recipient@gmail.com","Subject","File(txt).txt")
    message=addAttachment(message,"luffy.jpg.tiff")
    sendEmail(message,"*****")#Password for the email sender
    print(message)
if main()=="__main__":
    main()
