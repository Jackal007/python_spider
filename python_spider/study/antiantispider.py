# -*_coding:utf-8-*-
import requests
import re
from xlwt import Workbook
import time

'''
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}#构造头部
cook ={"Cookie":''}#cookie有改动，大家用自己的cookie就好
url="https://www.taobao.com/market/nvzhuang/dress.php?spm=a21bo.7723600.8224.2.nPpHHT"
#html=requests.get(url).content
html=requests.get(url,cookies=cook,headers=headers).content#get中提交url,COOKIE, 
print html
'''
def getHtml(url):
    proxylist = (
            '123.134.185.11',
            '115.228.107.142',
            '180.76.135.145',
            '58.218.198.61',
            '110.72.43.148',
            )
    for proxy in proxylist:
        proxies = {'': proxy}
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}  # 构造头部
    cook = {''}  # cookie有改动，大家用自己的cookie就好
    # html=requests.get(url).content
    html = requests.get(url, cookies=cook, headers=headers, proxies=proxies).text
    return html

def changeurl(start_url, page):  # 传参数(开始的url，页数)  
    urls = []
    for i in range(1, page + 1):
        url = start_url + str(i)
        urls.append(url)
    return urls
start_url = "https://list.tmall.com/search_product.htm?type=pc&totalPage=100&cat=50025135&sort=d&style=g&from=sn_1_cat-qp&active=1&jumpto="
urls = changeurl(start_url, 2)

wb = Workbook()
ws = wb.add_sheet('sheet1')
ws.write(0, 0, 'pid')
ws.write(0, 1, 'price')
ws.write(0, 2, 'title')
ws.write(0, 3, 'url')
index = 1
for url in urls:
    
    html = getHtml(url)
    time.sleep(1)
    reForProduct = re.compile('<div class="product  " data-id="(\d+)"[\s\S]+?<p class="productPrice">\s+<em title="(.+?)">[\s\S]+?<p class="productTitle">\s+<a href="(.+?)" target="_blank" title="(.+?)"[\s\S]+?<\/div>\s+<\/div>')
    products = reForProduct.findall(html)
    
     
    for pro in products:
        for (pid, price, url, title) in products:
            text = ("%s\t%s\t%s\t%s") % (pid, price, title, url)
            print (text)
            ws.write(index, 0, pid)
            ws.write(index, 1, price)
            ws.write(index, 2, title)
            ws.write(index, 3, url)
            index += 1

wb.save('result.xls')
