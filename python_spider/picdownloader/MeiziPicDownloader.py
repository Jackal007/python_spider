import requests, os, time, sys
from picdownloader import SetDownloader
from bs4 import BeautifulSoup

'''
抓取mzitu.com下的所有图片
'''

class MeiziPicDownloader():
    def __init__(self):
        self.site = 'http://www.mzitu.com/page/'
        
        
    def getPage(self, url):
        '''
        @url:url
                        获取当前链接的页面(顺便去掉没用的东西)
        '''
#         try:
        r = requests.get(url).content
        page = BeautifulSoup(r, from_encoding="GBK")
        return page
#         except:
#             return []
    
    def getSets(self, url):
        '''
        @url:url
                        获取当前链接的页面下的所有链接
        '''
        links, titles = [], []
#         try:
        page = self.getPage(url)
        # 图片链接
        for i in page.select('#pins')[0].select('a'):
            if i.string is not None:
                if 'http' not in i['href']:
                    i['href'] = self.site + i['href']
                links.append(i['href'])
                titles.append(i.string)
        return links, titles
#         except:
#             return []
            
    def broad(self, url):
        '''
                        广度优先小爬爬函数
        @url:网址
        '''
        
        # 先把当前页面的图片保存下来
        i = 1
        while True:
            # 将链接添加到数组的后面
            links, titles = self.getSets(self.site + str(i))
            for link, title in zip(links, titles):
                number = link.split('/')[-1]
                SetDownloader.SetDownloader(number, title).start()
            i += 1
                
    def start(self):
        print('big start')
        self.broad(self.site)
        print('big over')
    
if __name__ == '__main__':
    t = MeiziPicDownloader()
    t.start()
