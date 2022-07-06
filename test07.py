import pprint as pp
import time, requests

url = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw" #pg1-3填入框框 跑3個網址

pages = list()
for pg in range(1, 4):
    pages.append(url.format(pg))

for page in pages:
    html = requests.get(page).text
    pp.pprint(html)
    time.sleep(3)
    print("=========================")