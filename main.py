import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = requests.get("https://www.hankyung.com/realestate/article/2023053087646")
#bs = BeautifulSoup(html, 'html.parser')
print(html)
#
# #print(infos[0]["href"])
# #url = infos[0]["href"]
# url =
# response = requests.get(url)
# if response.status_code == 200:
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     print(html, soup)
# else:
#     print(response.status_code)


url = 'https://www.hankyung.com/ranking'
response = requests.get(url)

d = dict()
now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
print(now)

save=False

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    list = soup.select_one("#realtime_tab > div:nth-child(1) > ul")
    infos = list.select("h2 > a")
    for i in infos[:5]:
        d[i.get_text()] = i["href"]

    if save:
        df = pd.DataFrame({"제목": d.keys(), "링크": d.values()})
        df.to_csv(f"./db/{now}.csv")


else:
    print(response.status_code)


