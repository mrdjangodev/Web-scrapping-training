# <-- task -->
# take the price of ASUS TUF Gaming NVIDIA GeForce RTX 4080 OC Edition Video Card (PCIe 4.0, 16GB GDDR6X, HDMI 2.1, DisplayPort 1.4a, GPU Tweak) TUF-RTX4080-O16G-GAMING
# from this url -> https://www.newegg.ca/asus-geforce-rtx-4080-tuf-rtx4080-o16g-gaming/p/N82E16814126598?Item=N82E16814126598

from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/asus-geforce-rtx-4080-tuf-rtx4080-o16g-gaming/p/N82E16814126598?Item=N82E16814126598"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())/

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find('strong')
print(strong.string)

# completed