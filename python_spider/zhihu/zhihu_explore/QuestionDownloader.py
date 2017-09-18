'''
Created on 2017年9月16日

@author: zheng
'''

import requests
from bs4 import BeautifulSoup
from Tools import MyHeader
from Tools import MyProxy

class QuestionDownloader():
    def __init__(self, number):
        self.url = 'https://zhuanlan.zhihu.com/p/' + str(number)
        r = requests.get(self.url, headers=MyHeader.getHeader(), proxies=MyProxy.getProxy())
        print(r)
        soup = BeautifulSoup(r)
        self.title = soup.select('.TitleImage')[0].select('h1').string()
    
    def getTitle(self):
        return self.title
    
    def getContent(self):
        return self.content

if __name__ == '__main__':
    t = QuestionDownloader(24388271)
    print(t.getTitle())
