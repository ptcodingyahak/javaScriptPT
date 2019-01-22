from bs4 import BeautifulSoup
import re
import pymysql
from urllib.request import urlopen

conn = pymysql.connect(host='127.0.0.1',
                        port='3306', user='root', passwd='12345', db='mysql',
                        charset='utf8')

cur = conn.cursor()
cur.execute("USE wikipedia")

def pageScraped(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        return False
    page = cur.fetchone()

    cur.execute("SELECT * FROM links WHERE fromPageId = %s", (int(page[0])))
    if cur.rowcount == 0:
        return False
    return True

def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pafes (url) VALUES (%s)", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def insertLink(fromPageId, toPageId):
    cur.execute(
        "SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s",
        (int(fromPageId), int(toPageId))
    )
    if cur.rowcount == 0:
        cur.execute(
            "INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)",
            (int(fromPageId), int(toPageId))
        )
        conn.commit()

def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bs0bj = BeautifulSoup(html, "html.parser")
    for link in bs0bj.findAll("a", href=re.cpmpile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if not pageScraped(link.attrs['href']):
                            #Find new web page and insert link than find another pages.
            newPage = link.attrs['href']
            print(newPage)
            getLinks(newPage, recursionLevel+1)
        else:
            print("Skipping: "+str(link.attrs['href'])+" found on "+pageUrl)
getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()
