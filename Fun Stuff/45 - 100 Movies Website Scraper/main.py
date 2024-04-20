import random

from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/"
                        "best-movies-2/")
response.encoding = "utf-8"
movie_webpage = response.text
soup = BeautifulSoup(movie_webpage, "html.parser")

all_title_text = soup.find_all(class_="article-title-description__text")
all_title_raw_text = [item.find("h3").get_text() for item in all_title_text]
all_title_raw_text.reverse()

with open("movies.txt", "wt", encoding="utf-8") as file:
    for item in all_title_raw_text:
        file.write(item + '\n')

all_movies = []
with open("movies.txt", "r", encoding="utf-8") as file:
    for item in file:
        all_movies.append(item)

print(random.choice(all_movies))
