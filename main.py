import requests 
from bs4 import BeautifulSoup
import time
#คำสั่ง ลง module (pip) (ใช้ใน cmd)
#pip install requests
#pip install beautifulsoup4
url = "https://www.bilibili.tv/th/play/1035102"
x = requests.get(url)
soup = BeautifulSoup(x.text, 'html.parser')
mydivs = soup.find_all("p", {"class": "across-card__info_title"})
old_ep = 0
for ep in mydivs:
    ep = str(ep).split('<p class="across-card__info_title" style="--line:3;">')[1]
    ep = str(ep).split('</p>')[0]
    print(ep)
    print("")
    old_ep += 1

print("Total episode now is : ", count," EP ")

new = False
minutes = 1 * 60
while new == False:
    new_ep = 0
    url = "https://www.bilibili.tv/th/play/1035102"
    x = requests.get(url)
    soup = BeautifulSoup(x.text, 'html.parser')
    mydivs = soup.find_all("p", {"class": "across-card__info_title"})
    for ep in mydivs:
        ep = str(ep).split('<p class="across-card__info_title" style="--line:3;">')[1]
        ep = str(ep).split('</p>')[0]
        print(ep)
        new_ep += 1

    if new_ep > old_ep:
        new = True
        print("ตอนใหม่มาแล้ว")

    print("Total episode now is : ", count," ตอน")

    time.sleep(minutes)
    