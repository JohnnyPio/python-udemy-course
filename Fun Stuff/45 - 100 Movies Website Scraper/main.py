from bs4 import BeautifulSoup
import lxml

with open("website.html", "r", encoding="utf8") as file:
    contents = file.read()