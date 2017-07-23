import requests, os, time, sys
from bs4 import BeautifulSoup

'''
2.图片的命名机制
'''

class BeautyPicDownloader():
    def __init__(self):
        self.site = 'http://www.mzitu.com'
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
        @url:url
                        获取当前链接的页面下的所有链接
        '''
        links = []
        try:
            r = requests.get(url).content
            Page = BeautifulSoup(r, from_encoding="GBK")
            for i in Page.select('a'):
                if '#' in i['href']:
                    continue
                if 'http' not in i['href']:
                    i['href'] = self.site + i['href']
                links.append(i['href'])
            return links
        except:
            return []
        
    def getPics(self, url):
        '''
        @url:url
                        获取当前页面下的所有图片的内容
        '''
        pics, names = [], []
        try:
            r = requests.get(url).content
            Page = BeautifulSoup(r, from_encoding="GBK")
            for i in Page.select('img'):
                if 'http' not in i['src']:
                    i['src'] = self.site + i['src']
                names.append(i['src'])
            pics = [requests.get(i).content for i in names]
            names = [i.replace('http://', '').replace('https://', '').replace('/', '_').strip('.') \
                     for i in names]
            return pics, names
        except:
            return []
            
    def broad(self, url):
        '''
                        广度优先小爬爬函数
        @url:网址
        '''
        # 接下来要遍历的链接
        links = self.getLinks(url)
        # 先把当前页面的图片保存下来
        
        for link in links:
            print('getting page -->' + link)
            # 将链接添加到数组后
            links.extend(self.getLinks(link))
            links = list(set(links))
            pics, names = self.getPics(url)
            for pic, name in zip(pics, names) :
                self.savePic(name, pic)
                
    def start(self):
        print('start')
        self.broad(self.site)
        print('over')
    
if __name__ == '__main__':
    t = BeautyPicDownloader()
    t.start()
