print('get rubbish,and send them to my frieds ，哈哈哈哈哈')
from rubbishLetter import qiushibaike
from rubbishLetter import mailSender
import time

spider=qiushibaike.qiushibaikeSpider()
mailSender=mailSender.MailSender()
mailSender.setToAddresses(['956795145@qq.com','781210678@qq.com'])
while True:
    fun = spider.getWordFun()
    spider.storeToDataBase(fun)
    mailSender.getMsgs()
    mailSender.sendmail()
    time.sleep(3600)
