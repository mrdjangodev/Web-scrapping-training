from bs4 import BeautifulSoup

with open("try1/index.html", 'r') as f:
    doc = BeautifulSoup(f, "html.parser")

# tag = doc.title
# # print(tag)
# print(tag.string)
# #string -> works for taking data without tags


##<<-- finding tag -->>

# tag = doc.find('p')
# print(tag)

##<<-- finding multiple tags -->>
# tags = doc.find_all('p')
# print(tags)

# tags = doc.find_all('p')[0]
# print(tags)

tags = doc.find_all('p')[0]
print(tags.find_all('b'))