import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# sender = '2229238008@qq.com'
# receiver = 'chenhao15887805462@163.com'
class email:
    #发送单纯的文本
    def sendTextEmail(self):
        authcode = ''#授权码
        sender = 'chenhao15887805462@163.com'
        receiver = '2229238008@qq.com'
        subject = 'Python发送邮件测试'
        content = 'Hello World'
        msg = MIMEText(content)
        msg['subject'] = subject
        msg['from'] = sender
        msg['to'] = receiver
        try:
            s = smtplib.SMTP_SSL("smtp.163.com", 465)
            s.login(sender, authcode)
            s.sendmail(sender, receiver, msg.as_string())
            print("发送成功")
        except s.SMTPException as e:
            print("发送失败")

        finally:
            s.quit()
    #发送带附件的
    def SendAttEmail(self):
        authcode = ''#授权码
        sender = 'chenhao15887805462@163.com'
        receiver = '2229238008@qq.com'
        subject = 'Python发送邮件测试'
        content = 'Hello World'
        msg = MIMEMultipart('mixed')
        msg['Subject'] = subject
        msg['From'] = sender
        #多个收件人以;连接
        msg['To'] = receiver
        #文本内容
        text = 'Hello,WOrld'
        text_plain = MIMEText(text, 'plain', 'utf-8')
        msg.attach(text_plain)
        #附件
        file = open(r'/Users/chenhao/Documents/NJU/南京大学软件学院/周报/陈浩-本周工作总结(2018.10.15-10.21).xlsx', 'rb').read()
        text_file = MIMEText(file, 'base64', 'utf-8')
        text_file['Content-Type'] = 'application/octet-stream'
        text_file['Content-Disposition'] = 'attachment; filename="test.xlsx"'
        msg.attach(text_file)
        #fasong
        try:
            s = smtplib.SMTP_SSL("smtp.163.com", 465)
            s.login(sender, authcode)
            s.sendmail(sender, receiver, msg.as_string())
            print("发送成功")
        except s.SMTPException as e:
            print("发送失败")

        finally:
            s.quit()

# class
if __name__ == '__main__':
     email = email()
     email.SendAttEmail()