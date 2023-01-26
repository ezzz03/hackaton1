import csv

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag

URL = 'https://www.kivano.kg/mobilnye-telefony'

response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
cards = soup.find_all('div', class_='item')
result = []
for tag in cards:
    title = tag.find('div', class_='listbox_title oh').text
    price = tag.find('div', class_='listbox_price text-center').text
    image = tag.find('div', class_='listbox_img pull-left').find('img').get('src')
    obj = {
        'title': title,
        'price': price,
        'image': image
    }
    result.append(obj)


with open('telefony.csv', 'w') as file:
    names = ['title', 'price', 'image']
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writeheader()
    for phones in result:
        writer.writerow(phones)