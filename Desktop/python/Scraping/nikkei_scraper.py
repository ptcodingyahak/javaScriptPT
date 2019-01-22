from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.nikkei.com/")
bs0bj = BeautifulSoup(html.read(), "html.parser")

title_str = bs0bj.title
tt_str = title_str.string

print = (tt_str)


