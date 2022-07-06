import json, time, requests
from bs4 import BeautifulSoup
import sqlite3
sel = "section > div.mcont > div > p" #新聞內容
with open("nkustnews.json", "r", encoding="utf-8") as fp:
    news_link = json.loads(fp.read())
for link in news_link[2:]:
    url=link['herf']
    print(url)
    html= requests.get(url).text
    soup = BeautifulSoup(html, "html.parser") #解析資料
    data = soup.select(sel) #標籤名
    data = [str(d.text) for d in data]
    target = "".join(data)
    db=sqlite3.connect('nkustnews.db')
    cur=db.cursor()
    sql="insert into news (title, content, url, date) values(?,?,?,?)"
    data= (link['title'], target, link['herf'], link['data'])
    cur.execute(sql, data)
    db.commit()
    time.sleep(3) 