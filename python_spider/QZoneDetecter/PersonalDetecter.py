'''
Created on 2017年7月26日

0author: zhenglongtian
'''
import requests
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
    }

class PersonalDetecter():
    def __init__(self, qq='501962603'):
        self.site = 'https://user.qzone.qq.com/' + qq
        self.name = ''
        self.logindata = {
            'u':'3271816560',
            'p':'xxxs'}
    
    def getIssues(self):
        url = self.site
        session = requests.Session()
        session.post(url='qzs.qzone.qq.com/qzone/v5/', data=self.logindata, headers=headers)
        page = session.get(url)
        soup = BeautifulSoup(page.content)
        print(page.status_code)
        issues = soup.select('li[class="f-single f-s-s"]')
        print(issues)
        return issues
    
    def getContent(self, issue):
        content = issue.select('.f-info').string
        print(content)

if __name__ == '__main__':
    t = PersonalDetecter()
    a = t.getIssues()
    for i in a:
        t.getContent(i)
        
