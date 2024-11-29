# достать цены на квартиры адресс фотку если есть и ссылка

import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
import csv

url = 'https://stroka.kg/kupit-kvartiru/'

HEADER = {
    'user-agent' :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

baza = requests.get(url, headers=HEADER, verify=False)

soup = BeautifulSoup(baza.text, 'html.parser')

posts = soup.findAll('tbody', class_='topics-item')
# pp(block)

new_list = []

for item in posts:
        new_list.append({
                'price' : item.find('td', class_='topics-item-topic_cost topics-item-td').get('title'),
                'description' : item.find('td', class_='topics-item-topic_name').find('a').get_text('span'),
                 'link' : item.find('td', class_='topics-item-topic_name').find('a').get('href'),
        })
pp(new_list)

with open('fileTent.csv', 'a') as file:
    writer = csv.writer(file, delimiter= ';' )

    writer.writerow(['price', 'description', 'link'])

    for item in new_list:
        writer.writerow([item['price'],
                        item['description'],
                        item['link']])





