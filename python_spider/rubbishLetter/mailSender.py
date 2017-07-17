'''
Created on 2017年7月16日

@author: jack
'''
# encoding=utf-8
import smtplib 
from threading import Timer
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Tools import MyDataBase

class MailSender():
    def __init__(self):
        self.smtpServer = "smtp.126.com"
        self.user = "z6185091@126.com"
        self.pwd = "zz6691978"
        self.fromAdddress = "z6185091@126.com"
        self.toAddresses = []
        self.msgs = []
        
    def setToAddresses(self, toAddresses):
        self.toAddresses = toAddresses
        
    def getMsgs(self):
        db = MyDataBase.MyDataBase(database='rubbish_letter')
        conn = db.getConn()
        executer = db.getExcuter()
        executer.execute('select content from qiushibaike order by id desc limit 1')
        for i in executer.fetchall():
            self.msgs.append(i[0])
        
    
    def sendmail(self,):
        s = smtplib.SMTP()
        s.connect(self.smtpServer)  # 连接smtp服务器
        s.login(self.user, self.pwd)  # 登录邮箱
        # 给地址中的每一个人都发邮件
        for toAddress in self.toAddresses:
            for msg in self.msgs:
                mail_msg = MIMEMultipart()
                mail_msg['Subject'] = "不好意思，打扰了"
                mail_msg['From'] = self.fromAdddress
                mail_msg['To'] = ','.join(toAddress)
                mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))
                s.sendmail(self.fromAdddress, toAddress, mail_msg.as_string())  # 发送邮件
            
        s.quit()

if __name__ == '__main__':
    t = MailSender()
    t.setToAddresses(['z6185091@126.com'])
    t.getMsgs()
    t.sendmail()
