print('get rubbish,and send them to my frieds ，哈哈哈哈哈')
from rubbishLetter import qiushibaike
from rubbishLetter import mailSender
import time,random

spider=qiushibaike.qiushibaikeSpider()
mailSender=mailSender.MailSender()
mailSender.setToAddresses(['956795145@qq.com','781210678@qq.com','503098884@qq.com',\
                           '1162503985@qq.com','1169613431@qq.com','2998618011@qq.com',])
while True:
    fun = spider.getWordFun()
    spider.storeToDataBase(fun)
    mailSender.getMsgs()
    mailSender.sendmail()
    time.sleep(random.randint(60,7200))
