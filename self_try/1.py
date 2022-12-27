from bs4 import BeautifulSoup
import requests
import re

search_term = input("What are you searching for? ")

url = f"https://aliexpress.ru/category/202000005/home-appliances.html?spm=a2g2w.home.category.3.75df5931c8FCt0"
page = requests.get(url).text
print(page)
doc = BeautifulSoup(page, 'html.parser')
# print(doc)
page_text = doc.find(class_="store-filter clearfix w-100")
# print(page_text)
# not finished
