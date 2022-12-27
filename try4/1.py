from bs4 import BeautifulSoup
import requests
import re

searching_gpu = input("What product do you want to search for?")

url = f"https://www.newegg.ca/p/pl?d={searching_gpu}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, 'html.parser')

page_text = doc.find(class_="list-tool-pagination-text")
num_pages = int(str(page_text.strong).split("/")[-2].split(">")[-1][:-1]) #number of pages

items_found = {}

for pg in range(1, num_pages+1):
    url = f"https://www.newegg.ca/p/pl?d={searching_gpu}&N=4131"
    page = requests.get(url).text
    doc = BeautifulSoup(page, 'html.parser')

    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text=re.compile(searching_gpu))
    # print(items)
    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue
        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        price = next_parent.find(class_="price-current").strong.string

        items_found[item] = {
            "price": int(price.replace(",", '')),
            "link": link,
        }

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])


for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print('-------------------------------------------------------')