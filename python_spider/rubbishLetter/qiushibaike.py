'''
Created on 2017年7月16日

@author: jack
'''
from bs4 import BeautifulSoup
from Tools import MyDataBase
import requests
import os

class qiushibaikeSpider:
    def __init__(self):
        self.siteURL = 'https://www.qiushibaike.com'
        
    def getPage(self, index):
        url = self.siteURL + '/8hr/page/' + str(index)+'/?s=5000638'
        print('getting page ', index)
        return requests.get(url).content
    
    def getWordFun(self, num=1, level=1000, comment=50):
        '''
                        获取文字的笑话，即没有图片的笑话
        num:笑话的数量
        level:笑话的质量，按点赞数算
        comment:评论数
        '''
        fun = []
        index = 1
        while True:
            page = self.getPage(index)
            index += 1
            level -= 100  # 越到后面 笑话质量越不好
            soup = BeautifulSoup(page)
            for i in soup.select('div[class="article block untagged mb15"]'):
                block = BeautifulSoup(str(i))
                pic = block.select('img')
                # 没有图片才继续操作
                if len(pic) <= 1:
                    content = block.select('.content > span')[0].string
                    vote = int(block.select('.stats-vote > i')[0].string)
                    if vote > level:
                        fun.append(content)
            if len(fun) > num:
                break
        return fun
    
    def storeToDataBase(self, fun):
        db = MyDataBase.MyDataBase()
        conn = db.getConn()
        executer = db.getExcuter()
        for i in fun:
            
            sql='insert into qiushibaike(content) values("' + i + '")'
            executer.execute(sql)

if __name__ == '__main__':
    t = qiushibaikeSpider()
    fun = t.getWordFun()
    t.storeToDataBase(fun)
