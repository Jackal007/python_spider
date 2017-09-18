'''
Created on 2017年9月18日

@author: zheng
'''
import requests
from bs4 import BeautifulSoup
from Tools import MyHeader
from Tools import MyProxy


class car():
    def __init__(self):
        self.url = 'http://xm.58.com/ershouche/'
    
    def getPage(self):
        r = requests.get(self.url, headers=MyHeader.getHeader(), proxies=MyProxy.getProxy())
        print(r)
        return r
    
    def haha(self):
        soup = BeautifulSoup(self.getPage())
#         car_list = soup.select("ul[class='car_list ac_container']")
#         first_car = car_list.select_one('li[class="clearfix car_list_less ac_item"] div[class="col col2"] a h1')
#         print(first_car.string)
    
if __name__ == '__main__':
    t = car()
    t.haha()
