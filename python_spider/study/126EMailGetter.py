import requests
import re

def emailGetter(email,password):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
    }
    params = {
        'df': 'mail126_letter',
        'from': 'web',
        'funcid': 'loginone',
        'iframe': '1',
        'language': '-1',
        'passtype': '1',
        'product': 'mail126',
        'verifycookie': '-1',
        'net': 'failed',
        'style': '-1',
        'race': '-2_-2_-2_db',
        'uid': email,
        'hid': '10010102'
    }
    postdata = {
        "username": email,
        "savelogin": "1",
        "url2": "http://mail.126.com/errorpage/error126.htm",
        "password": password
    }
    
    #先建立一个会话
    url='http://126.com'
    session=requests.session()
    session.get("http://126.com", headers=headers)
    
    url = "https://mail.126.com/entry/cgi/ntesdoor?"
    
    #然后登录
    login = session.post(url, data=postdata, headers=headers, params=params)
    pattern = re.compile(r'href = "(.*?)"')
    result = re.findall(pattern, login.text)
    index_page = session.get(result[0])
    pattern = re.compile(r"('messageCount'.*?).*?('unreadMessageCount'.*?),")
    res_index = re.findall(pattern, index_page.text)
    print(res_index)

    return index_page

if __name__ == '__main__':
    email = input('请输入你的 email\n>  ')
    secret = input("请输入你的密码\n>  ")
    emailGetter(email, secret)