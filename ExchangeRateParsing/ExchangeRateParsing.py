import requests
from bs4 import BeautifulSoup
import csv
all_exchange_rate_list = []
all_titles_list = []

#url = "https://ru.myfin.by/currency/moskva"
#
#headers = {
#    "Accept": "*/*",
#    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
#}
#
#req = requests.get(url, headers=headers)
#src = req.text
#
#with open("page.html", "w",encoding="utf8") as file:
#   file.write(src)

with open("page.html",encoding="utf8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_titles = soup.find_all(class_="title")
for item in all_titles:
#    print(item.text)
    all_titles_list.append(item.text)
all_exchange_rate = soup.find_all(class_="cbr_today")
for item in all_exchange_rate:
#    print(item.text)
    all_exchange_rate_list.append(item.text)
with open("table.csv","w") as file:
    writer = csv.writer(file,delimiter=";")
    writer.writerows([all_titles_list,all_exchange_rate_list])
print(all_exchange_rate_list)