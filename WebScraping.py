# import requests
# import bs4
# from bs4 import BeautifulSoup
# import pprint
# req= requests.get("https://news.ycombinator.com")
# par= BeautifulSoup(req.text,"html.parser")
# votes= par.select(".score")
# links=par.select(".storylink")
# #print(votes)
# #print(links)
# data=[]
# for l,h in enumerate(links):
#     link=links[l].getText()
#     vote=votes[l].
#     data.append(link)
# print(data)
from bs4 import BeautifulSoup
import requests

url="https://news.google.co.in/"
code=requests.get(url)
soup=BeautifulSoup(code.text,'html5lib')
for title in soup.find_all('span',class_="titletext"):
    print(title.text)