import requests

from bs4 import BeautifulSoup

import csv

# from selenium import webdriver
#
# from webdriver.chrome import ChromeDriverManager
#
# from selenium.webdriver.chrome.service import Service

URL = 'https://lalafo.kg/'


HOST = 'https://lalafo.kg/kyrgyzstan/q-%D0%B0%D0%B9%D1%84%D0%BE%D0%BD%D1%8B'

HEADER =  {
        "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

}

r = requests.get(URL, headers=HEADER, verify=False)

soup = BeautifulSoup(r.text, 'html.parser')

smartBOX = soup.findall("div", class_="row")

print(smartBOX)

new_list = []


for item in smartBOX:
        new_list.append({
                "title" : item.find('div', class_='AdTileHorizontalDescription').find('a').get('href'),
                "price" : item.find('p', class_='AdTileHorizontalPrice').get_text(),
                "image" : item.find('div', class_='AdTileHorizontalImage').find('a').get('href'),



})
print(new_list)




