from  bs4 import BeautifulSoup
import requests
import re
import lxml

url = "https://realpython.com/atom.xml"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'xml')
entries = soup.find_all("entry")

res_dict = {}

for entry in entries:
    title = entry.title
    res_dict[title.string] = {}
    link = entry.link
    summary = entry.summary
    updated = entry.updated

    res_dict[title.string]["link"]=link.string
    res_dict[title.string]["summary"]=summary.string
    res_dict[title.string]["updated"]=updated.string
print(res_dict)