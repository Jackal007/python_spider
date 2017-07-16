from bs4 import BeautifulSoup
import requests
import re
import os

class Spider:
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
        
    def getPage(self, pageIndex):
        url = self.siteURL + '?page=' + str(pageIndex)
        r = requests.get(url)
        return r.text
        
    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, page)
        for item in items:
            print(item[0],item[1],item[2],item[3],item[4])
    
    def saveBrief(self, content, name):
        pass
    
    def mkdir(self, path):
        path = path.strip()
        if not os.path.exists(path):
            os.makedirs(path)
            return True
        else:
            return False
    
    def getName(self, content):
        soup = BeautifulSoup(content)
        all=soup.select('.lady-name')
        names=[]
        for i in all:
            name=BeautifulSoup(str(i)).a.string
            names.append(name)
        return names
        

t = Spider()
content = t.getPage(1)
names = t.getName(content)
for i in names :
    print(i)
'''
这里学到了面向对象的爬虫，写起来比较好
但是这边的解析就只用了普通的正则表达式
我觉得得使用更高档的写法
'''
        
