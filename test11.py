import requests, time
url ="https://stats.moe.gov.tw/files/detail/{0}/{0}_student.csv"
links= [(year,url.format(year)) for year in range(103,111)] #(年,網址)
for link in links:
    csvdata= requests.get(link[1]).text #links[0=year,1=網址]
    with open("studata-{}.csv".format(link[0]), "w", encoding="utf-8", newline="") as fp:
        fp.write(csvdata)
    time.sleep(3)
print("done")