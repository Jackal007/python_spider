from bs4 import BeautifulSoup
html = """
<a class="lady-name" href="//mm.taobao.com/self/model_card.htm?user_id=687471686" target="_blank">田媛媛</a>
"""

soup=BeautifulSoup(html)
print(soup.a.string)
