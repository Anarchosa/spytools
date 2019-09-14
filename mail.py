#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet OTOMAIL")

me = input("Mail adresiniz:")
you = input("Kullanıcı Maillerinin Listesini Girin (sadec gmail): ")
passwd=input("Mail Sifrenizi Girin: ")
mesaj=input("Gondereceginiz Mailin Icerigi (html syntaxi ile yazılmıs metin dosyası): ")
baslik=input("Email Konusunu Girin: ")

file=open(you,"r")
file=file.read()
file=file.split()


msg = MIMEMultipart('alternative')
msg['Subject'] = baslik
msg['From'] = me
msg['To'] = you


# Create the body of the message (a plain-text and an HTML version).
#text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
y=open(mesaj,"r")
y=y.read()

# Record the MIME types of both parts - text/plain and text/html.
#part1 = MIMEText(text, 'plain')
part2 = MIMEText(y, 'html')


#msg.attach(part1)
msg.attach(part2)
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login(me, passwd)
for i in file:
    mail.sendmail(me, i, msg.as_string())
mail.quit()

