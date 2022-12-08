* [X] 1 Introduction
* [X] 2 Beautiful Soup 4 setup

  ```
  pip install beautifulsoup4
  ```
* [X] 3 Reading HTML files

  ```
  from bs4 import BeautifulSoup

  with open("index.html", 'r') as f:
      doc = BeautifulSoup(f, "html.parser")
  print(doc.prettify())
  #prettify -> is function for printing my data pretty
  ```
* [X] 4 Find by tag name

  ```
  tag = doc.find('p')
  print(tag)
  ```
  *By the* `find() ` *function we can take only first one of our searched tags*
* [X] 5 Find all by tag name

  ```
  tags = doc.find_all('p')
  print(tags)
  ```
* [ ] 6 Parsing website html
* [ ] 7 Location text
* [ ] 8 Beautiful Soup Tress structure
