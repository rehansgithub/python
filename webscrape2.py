#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#print(soup) 

items = soup.find_all('div', class_='grid grid-cols-1 gap-4 sm:grid-cols-3')

for i in items:
    count = 1
    item = i.find_all('div', class_='w-full rounded border')
    for x in item:
        itemName = x.find('h4').text.strip('\n')
        itemPrice = x.find('h5').text
        print(f"{count} Price:{itemPrice}, Item Name:{itemName}")
        count+=1


pages = soup.find('nav', class_='pagination')
urls = []
links = pages.find_all('a')
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)
#print(urls)


count = 1
for i in urls:
    newUrl = url + i
    respone = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
#print(soup) 

    items = soup.find_all('div', class_='grid grid-cols-1 gap-4 sm:grid-cols-3')

    for i in items:
        
        item = i.find_all('div', class_='w-full rounded border')
        for x in item:
            itemName = x.find('h4').text.strip('\n')
            itemPrice = x.find('h5').text
            print(f"{count} Price:{itemPrice}, Item Name:{itemName}")
            count+=1
