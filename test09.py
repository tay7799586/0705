# import csv
# links=list()
# url = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw" 
# for pg in range(1,11):
#     links.append((pg, url.format(pg)))
# print(links)

# with open('links.csv', 'w', encoding='utf-8', newline='') as fp:
#     csvwriter = csv.writer(fp)
#     csvwriter.writerow([';page','link'])
#     csvwriter.writerows(links) #一次寫完
# print("done")

#簡化寫法 
import csv
url = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw" 
links=[(pg, url.format(pg)) for pg in range(1,11)] #串列生成式，用來產生串列10頁的資料型態

with open('links.csv', 'w', encoding='utf-8', newline='') as fp:
    csvwriter = csv.writer(fp)
    csvwriter.writerow(['page','link'])
    csvwriter.writerows(links) #一次寫完
print("done")


