from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.nikkei.com/")
bs0bj = BeautifulSoup(html.read(), "html.parser")

nameList = bs0bj.findAll("div", {"id":"CONTENTS"})
for name in nameList:
    print(name.get_text())

