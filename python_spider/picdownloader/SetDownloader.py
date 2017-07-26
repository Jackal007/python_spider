import requests, os, time, sys
from bs4 import BeautifulSoup

'''
抓取一个标题下的所有美女图片
'''

class SetDownloader():
    def __init__(self, number, title):
        self.site = 'http://www.mzitu.com/' + number
        self.directory = 'G://mzpics'
        self.title = title
        # 创建保存图片用的文件夹
        try:
            os.makedirs(self.directory + '/' + self.title)
#             os.mkdir(self.directory)
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
                with open(self.directory + '/' + self.title + '/' + name + '', 'wb') as pic:
                    pic.write(content)
            except:
                pass
        
    def getPage(self, url):
        '''
        @url:url
                        获取当前链接的页面(顺便去掉没用的东西)
        '''
        try:
            r = requests.get(url).content
            page = BeautifulSoup(r, from_encoding="GBK")
            return page
        except:
            return []
    
    def getLinks(self, url):
        '''
        @url:url
                        获取当前链接的页面下的所有链接
        '''
        links = []
        try:
            page = self.getPage(url)
            for i in page.select('.pagenavi')[0].select('a'):
                if 'http' not in i['href']:
                    i['href'] = self.site + i['href']
                if '上一' in i.span.string \
                or '下一' in i.span.string:
                    continue
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
            page = self.getPage(url)
            for i in page.select('.main-image')[0].select('img'):
                if 'http' not in i['src']:
                    i['src'] = self.site + i['src']
                names.append(i['src'])
            pics = [requests.get(i).content for i in names]
            names = [i.split('/')[-1] for i in names]
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
        i = 0
        while i < len(links):
            print('getting page -->' + links[i])
            # 先保存改页面的图片
            pics, names = self.getPics(links[i])
            for pic, name in zip(pics, names) :
                self.savePic(name, pic)
            # 将链接添加到数组的后面
            links.extend(self.getLinks(links[i]))
            # 对保存的链接进行去重，排序
            links = [i for i in set(links)]
            links = sorted(links, key=lambda l:int(l.split('/')[-1]))
            print(links)
            i += 1
                
    def start(self):
        print('start')
        self.broad(self.site)
        print('over')
    
if __name__ == '__main__':
    t = SetDownloader('95084', 'hh')
    t.start()
