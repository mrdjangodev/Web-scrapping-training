from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents
# print(trs[0].next_sibling) #next elemnt
# print(trs[1].previous_sibling) #previous element
# print(list(trs[0].next_siblings)) #all next elements

# 3 Tree Parents and Descendants
# ------------------parent--------------
# print(trs[0].parent.name)

# ----------- descendants --------
#  decendants gives us everything comes after or inside of this tag
# print(list(trs[0].descendants))
# print(list(trs[0].children)) # does the same work with descendants
# print(list(trs[0].contents)) # does the same work with descendants

prices = {}

for tr in trs[:10]:
    name, price =  tr.contents[2:4]
    # print(name.p.string)
    # print()
    fixed_name = name.p.string

    # print(price.span.string)
    # print()
    fixed_price = price.span.string
    prices[fixed_name] = fixed_price
print(prices)