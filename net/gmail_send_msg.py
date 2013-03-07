#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText


def gmail(user_from, user_to, pw, msg_text):
	s = smtplib.SMTP("smtp.gmail.com",587)
	s.ehlo()
	s.starttls()
	#s.ehlo
	s.login(user_from, pw)
	s.sendmail(user_from, user_to, msg_text)
	s.close()

if __name__ == '__main__':
	Password = ''
	Subject = "中文標題"
	Content = "中文內容測試"


	msg = MIMEText(Content, 'html', 'utf-8')
	msg['Subject'] = Subject
	msg['From'] = 'angel@heaven.org'
	msg['To'] = 'letoh.tw@gmail.com'

	gmail('mengcheng@gmail.com', ['letoh.tw@gmail.com'], Password, msg.as_string())


