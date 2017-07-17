'''
Created on 2017年7月16日

@author: jack
'''
from bs4 import BeautifulSoup
from Tools import MyDataBase
import requests, os, random

class qiushibaikeSpider:
    def __init__(self):
        # 伟大的爬虫所需要的内容
        self.siteURL = 'https://www.qiushibaike.com'
        self.headers = []
        self.proxies = []
        
        db = MyDataBase.MyDataBase(database='spider')
        executer = db.getExcuter()
        
        # 获取headers池的所有suer-agent
        executer.execute('select * from user_agent')
        for i in executer.fetchall():
            self.headers.append({'User-Agent':i[0]})
        
        # 获取proxy池的所有proxy
        executer.execute('select * from proxy')
        for i in executer.fetchall():
            self.proxies.append( {'': i[0]})
        
        db.close()
        
    def getPage(self, index):
        '''
                        获得页面内容
        @index:页码
        '''
        url = self.siteURL + '/8hr/page/' + str(index) + '/?s=5000638'
        print('getting page ', index)
        headers = self.headers[random.randint(0, len(self.headers) - 1)]
        proxy = self.proxies[random.randint(0, len(self.proxies) - 1)]
        page = requests.get(url, headers=headers , proxies=proxy)
        return page.content
            
    def getWordFun(self, num=1, level=1000, comment=50):
        '''
                        获取文字的笑话，即没有图片的笑话
        @num:笑话的数量
        @level:笑话的质量，按点赞数算
        @comment:评论数
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
        '''
                        把笑话保存到数据库
        @fun:笑话内容
        '''
        db = MyDataBase.MyDataBase(database='rubbish_letter')
        executer = db.getExcuter()
        
        for i in fun:
            try:
                print(i)
                i = i.replace('"', '')
                sql = 'insert into qiushibaike(content) values("' + i + '")'
                executer.execute(sql)
            except:
                continue
        
        db.close()

if __name__ == '__main__':
    t = qiushibaikeSpider()
    fun = t.getWordFun()
    t.storeToDataBase(fun)
