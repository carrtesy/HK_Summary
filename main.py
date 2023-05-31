import requests
from bs4 import BeautifulSoup

url = 'https://www.hankyung.com/ranking'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    list = soup.select_one("#realtime_tab > div:nth-child(1) > ul")
    infos = list.select("h2 > a")
    for i in infos:
        print(i.get_text())
        print(i["href"])
else:
    print(response.status_code)