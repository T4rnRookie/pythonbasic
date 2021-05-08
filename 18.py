import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
nyt_html = r.text

soup = BeautifulSoup(nyt_html,features="html.parser")
for h2 in soup.find_all("p"):
	print(h2.text)