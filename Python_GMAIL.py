#https://myaccount.google.com/apppasswords

import smtplib, ssl
from email.message import EmailMessage
import imghdr
smtp_server = "smtp.gmail.com"
port = 587 #For starttls
sender_email = "aleksgruntal@gmail.com"
password = input("parool") # gmail password
context = ssl.create_default_context()
#msg="Tere tulemast!"
msg = EmailMessage()
msg.set_content("Tere tulemast! Olen kirja keha!")
msg["Subject"]="Kirja teema"
msg["From"]="Aleksander Grüntal Logitpv23" #Nimi ka saab kirjutada #kellelt
msg["To"]="marina.oleinik@tthk.ee" #kellele
with open ("bee.jpg","rb") as fpilt:
    pilt=fpilt.read()
msg.add_attachment(pilt,maintype="image",subtype=imghdr.what(None, pilt))
try:
    server = smtplib.SMTP(smtp_server,port)
    server.starttls(context=context) #Secure the connection
    server.login(sender_email, password)
    server.send_message(msg) #server.sendmail(sendmail_email,to_email,msg)
    print("Kiri on saadetud")
except Exception as e:
    print(e)
finally:
    server.quit()