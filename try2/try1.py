from bs4 import BeautifulSoup
import re  # regular expression


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

# # Find class names
# tags = doc.find_all(class_="btn-item")
# print(tags)

# # Find regular expressions
# tags = doc.find_all(text=re.compile("\$.*"))
# print(tags)
# for tag in tags:
#     print(tag.strip())

# # Find limits
# tags = doc.find_all(text=re.compile("\$.*"), limit=1)
# for tag in tags:
#     print(tag.strip())


# Save modified HTML
# tags = doc.find_all("input", type="text")
# for tag in tags:
#     tag['placeholder'] = "Placeholder changed" 

# with open("modified.html", 'w') as file:
#     file.write(str(doc))