from email import message
import smtplib as s

ob=s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('sender@gmail.com','pass')
subject="test python mail"
body="i love python"
message="subject:{}\n\n{}".format(subject,body)
listadd=['testrec1@gmail.com', 'testrec1@gmail.com']
ob.sendmail('sender@gmail.com', listadd, message)
print("send email")