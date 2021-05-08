import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/section/world/africa'
r = requests.get(url)
nyt_html = r.text

soup = BeautifulSoup(nyt_html,features="html.parser")
for h2 in soup.findAll("h2", class_="e1xfvim30"):
	print(h2.text)