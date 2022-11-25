import smtplib
from getpass import getpass

serverMail = smtplib.SMTP_SSL('smtp.yandex.ru:465')
serverMail.login("email@email.ru", "password")
serverMail.auth_plain()

serverMail.set_debuglevel(1)

serverMail.sendmail("от кого",
                    "кому", "тело письма")


serverMail.quit()
