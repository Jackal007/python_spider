'''
Created on 2017年7月2日

@author: zhenglongtian
'''
import requests
import re

url = 'https://www.google.com.hk'

response = requests.get(url)
# 获得表单的提交地址
pattern = re.compile(r'<form .*action=".*".*method=".*>')
actions = re.findall(pattern, response.text)
prefix = re.compile(r'<form .*action="')
suffix = re.compile(r'".* method=".*>')
address = []

for i in actions:
    address.append(suffix.sub('', prefix.sub('', i)))

data = {
    'word':'',
    'pn':0,
    'rn' :10,
    'enc':'utf8'
    }
# keyword=input("please input the thing you want to know:")
# data['word']=keyword

print(len(actions))

# for i in address:
#     r=requests.post(url+i,params=data)
#     print(r.url)
#     with open(keyword+'.html','wb')as f:
#         f.write(r.content)
