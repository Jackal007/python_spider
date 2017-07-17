import requests, os, time
from bs4 import BeautifulSoup

try:
    os.mkdir('pics')
except:
    pass

url = 'https://tieba.baidu.com/f?kw=%C3%C0%C5%AE&fr=ala0&tpl=5'
page = BeautifulSoup(requests.get(url).content)
pics = page.select('img')
print(len(pics))
for i in pics:
    print(i['src'])
    try:
        pic = requests.get(i['src']).content
    except:
        pic = requests.get(url + i['src']).content
    name = i['src'].replace('http://', '').replace('https://', '').replace('/', '_')
    with open('pics/' + '1.jpg', 'ab') as f:
        f.write(pic)
