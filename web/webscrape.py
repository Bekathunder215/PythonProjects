import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.kathimerini.gr/"
req = requests.get(url)
soup = BeautifulSoup(req.content, "lxml")
title = soup.find_all("div", {"class":"media-content"})
with open("web/urlscrapeddata.txt", 'w') as f:
    for i in range(10):
        f.write(title[i].getText())