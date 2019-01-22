from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen ("https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=228")
bs0bj = BeautifulSoup(html.read(). "html.parser")

nameList = bs0bj.findAll("div", {"id":""}) #
for name in nameList:
    print(name.get_text())


