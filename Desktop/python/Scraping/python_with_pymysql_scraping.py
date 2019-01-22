from urllib.request import urlopen #
from bs4 import BeautifulSoup #The Scrapipng library importing python
import re #regular exprexpression function import
import datetime #make datetime function
import random #make randaom number function
import pymysql #Python import Mysql

conn = pymysql.connect(host='127.0.0.1',
                    user='root', passwd='12345', db='mysql', charset='utf8') #conn connect object with mysql

cur = conn.cursor() #cur is maked in connection with Mysql cor = corsor
cur.execute("USE scraping") #.exectue is to query with mysql

random.seed(datetime.datetime.now()) #"random.seed" = seed is to make first random number

def store(title, content): #"store" def = put into mysql with webPage source // def() is declaration function and than in the () is function parameter. #entirely, this function is insert in mysql content and title data.
    cur.execute(
        "INSERT INTO
         (title, content) VALUES (\"%s\", \"%s\")", #INSERT is mysql query sentence.
        (title, content)
    )
    cur.connection.commit() #commit() is in connection function commit() is DML language

def getLinks(articleUrl): #
    html = urlopen("http://en.wikipedia.org"+articleUrl) #Load urlopen and conncet articleUrl function
    bsObj = BeautifulSoup(html, "html.parser") #BeautifulSoup function have analys domain parsing
    title = bsObj.find("h1").get_text() #Contain domain data in bsObj and than find class and than input "title" parameter. // The get_text() all delete tag and make text
    content = bsObj.find("div", {"id":"mw-content-text"}).find("p").get_text() #Its like previous parameter with title but this parameter is search has "content" date.
    store(title, content) #
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a", # "a" has include all href
                    href=re.compile("^(/wiki/)((?!:).)*$")) #href means hypertext reference // re.compile() into the () is maked compiled data.

links = getLinks("/wiki/Kevin_Bacon")
try:
    while len(links) > 0: #python function "len" is count the number
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"] # random.randint() is to inside () include (minimum, maximum)
        print(newArticle)
        links = getLinks(newArticle)

except AttributeError:
    pass

finally:
    cur.close()
    conn.close()
