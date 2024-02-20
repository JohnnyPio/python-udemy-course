from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
title_line_info = soup.find_all(class_="titleline")
sub_text_info = soup.find_all(class_="score")

# List comprehension instead of for loops
all_titles = [title.find("a").get_text() for title in title_line_info]
all_links = [title.find("a").get("href") for title in title_line_info]
all_scores = [int(item.get_text().split()[0]) for item in sub_text_info]

most_upvotes_index = all_scores.index(max(all_scores))
print(all_titles[most_upvotes_index], all_links[most_upvotes_index])
