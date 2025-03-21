from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name = "a", class_ = "storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_ = "score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_index = article_upvotes.index(max(article_upvotes))
print(article_upvotes[max_index])
print(f"Max upvote belongs to {article_texts[max_index]}, {article_links[max_index]}")
