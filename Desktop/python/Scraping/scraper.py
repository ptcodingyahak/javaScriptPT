from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://ko.wikipedia.org/wiki/%EC%BB%B4%ED%93%A8%ED%84%B0")
bs0bj = BeautifulSoup(html.read(), "html.parser")

nameList = bs0bj.findAll("div", {"class":"toc"})
for name in nameList:
    print(name.get_text())



