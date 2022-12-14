from bs4 import BeautifulSoup

with open("try2/index2.html", 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')

tag = doc.find("option")
print(tag)
tag['selected'] = True
tag['value'] = "Changed value"
print(tag)