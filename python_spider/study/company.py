import requests

url = 'http://httpbin.org/cookies/set/number/123456789'

headers = {
     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    }

data = {
    'name':'jackal'
    }

session=requests.Session()
response=session.get(url)
print(response.text)
response=session.get('http://httpbin.org/cookies')
print(response.text)
