from bs4 import BeautifulSoup

with open("try2/index2.html", 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')

# # searching for tags
# tag = doc.find("option")
# print(tag)
# tag['selected'] = True
# tag['value'] = "Changed value"
# print(tag)
# print(tag.attrs) # finding tag attributes


# # finding multiple tags
# tags = doc.find_all(['p', 'div', 'li'])
# print(tags)

# # finding attributes
# tags = doc.find_all('option', text="Undergraduate")
# print(tags)


# Find class names
tags = doc.find_all(class_="btn-item")
print(tags)