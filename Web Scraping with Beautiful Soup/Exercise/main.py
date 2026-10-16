from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

headings = soup.find_all(name = "span", class_ = "titleline")
article_texts =  []
article_links = []
for heading in headings:
    text = heading.getText()
    article_texts.append(text)
    link = heading.find("a").get("href")
    article_links.append(link)

article_upvote = [int(upvotes.getText().split()[0]) for upvotes in soup.find_all(name = "span", class_ = "score")]
print(article_texts)
print(article_links)
print(article_upvote)

highest_upvote = max(article_upvote)
highest_upvote_article = article_upvote.index(highest_upvote)
print(article_texts[highest_upvote_article])
print(article_links[highest_upvote_article])

# for heading in headings:
#     print(heading.text)