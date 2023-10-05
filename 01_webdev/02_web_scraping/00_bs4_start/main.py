from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title.string)

# print(soup.prettify())

# print(soup.a) # prints first `a tag` it finds

# print(soup.find_all(name="a"))
# for tag in soup.find_all(name="a"):
#     print(tag.text)

# print(soup.find(name="h1", id="name"))
# print(soup.find(name="h3", class_="heading"))
# print(soup.select_one("p a"))
# print((soup.select("p a")))
