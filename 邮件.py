import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['subject'] = 'test'
msg['from'] = '13914082195@163.com'
msg['to'] = '1179386257@qq.com'
content = "你好，这是一封自动发送的邮件。"
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp=smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('13914082195@163.com','zjj971102')
smtp.sendmail('13914082195@163.com', '1179386257@qq.com', str(msg))
smtp.quit()

