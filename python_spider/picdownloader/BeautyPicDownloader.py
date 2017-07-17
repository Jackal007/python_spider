import requests, os, time, sys
from bs4 import BeautifulSoup

'''
1.跑过的网址不要跑
2.图片的命名机制
3.只下载高质量的图片
'''

class BeautyPicDownloader():
    def __init__(self):
        self.site = 'http://zhaofuli.mobi/'
        self.directory = 'pics'
        # 创建保存图片用的文件夹
        try:
            os.mkdir(self.directory)
        except:
            pass
        
    def savePic(self, name, content):
        '''
        @name:图片名
        @content:图片内容
        '''        
        # 保存图片
        if sys.getsizeof(content) > 20480:
            print('save picture ', name)
            try:
                with open(self.directory + '/' + name + '.jpg', 'wb') as pic:
                    pic.write(content)
            except:
                pass
        
    def getLinks(self, url):
        '''
                        获取当前页面下的所有链接
        '''
        links = []
        try:
            r = requests.get(url).content
            Page = BeautifulSoup(r)
            links = [i['href'] for i in Page.select('a')]
        except:
            pass
        return links
        
    def getPics(self, url):
        '''
                        获取当前页面下的所有图片内容
        '''
        pics, names = [], []
        try:
            r = requests.get(url).content
            Page = BeautifulSoup(r)
            names = [i['src'] for i in Page.select('img')]
            pics = [requests.get(i).content for i in names]
            names = [i.replace('http://', '').replace('https://', '').replace('/', '_') for i in names]
        except:
            pass
        return pics, names
    
    def deep(self, url):
        '''
                    深度优先小爬爬函数
        @url:网址
        '''
        # 先把当前页面的图片保存下来
        pics, names = self.getPics(url)
        for pic, name in zip(pics, names) :
            self.savePic(name, pic)
        
        links = self.getLinks(url)
        for link in links:
            self.deep(link)
            
    def broad(self, url):
        '''
                        广度优先小爬爬函数
        @url:网址
        '''
        # 先把当前页面的图片保存下来
        pics = self.getPics(url)
        for pic in pics :
            self.savePic(str(time.time()), pic)
        
        # 接下来要遍历的链接
        links = self.getLinks(url)
        for link in links:
            # 将链接添加到数组后
            links.extend(self.getLinks(link))
            links = list(set(links))
            pics = self.getPics(url)
            for pic in pics :
                self.savePic(str(time.time()), pic)
                
    def start(self):
        print('start')
        self.broad(self.site)
        print('over')
    
if __name__ == '__main__':
    t = BeautyPicDownloader()
    t.start()
