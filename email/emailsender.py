#go to mail 
#security and two factor authentification
#"app passwords"
#add the python project, get a key!, and save it!
#for this problem our key is going to be key = keyblahblah

import email.message
import ssl
import smtplib #we import ssl and smtplib protocol to send mail to any internet machine

email_sender = "bekathunder215@thunder.com"
email_password = "password123!"
#the email reciever you can get from website temp-mail.org
email_receiver = "temporarymail@someone.com??" 
subject = "This is a subject of the email"
body = """\
    When you open the email, you will see the body object.\
          So right now i can write a big 5000 word letter.\
            """

#we put the mail details in...
eml = email.message.EmailMessage()
eml["From"] = email_sender
eml["To"] = email_receiver
eml["Subject"] = subject
eml.set_content(body)

context = ssl.create_default_context() 
#we use the default port and the gmail smtp protocol
with smtplib.SMTP_SSL("smtp.gamil.com", 456, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, eml.as_string())