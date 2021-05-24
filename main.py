from bs4 import BeautifulSoup
import requests

respone_html = requests.get("https://news.ycombinator.com/news").text

soup = BeautifulSoup(respone_html, "html.parser")

title_article = []



article_text = [tag.text for tag in soup.find_all(name='a', class_="storylink")]
article_score = [tag.text for tag in soup.find_all(name='span', class_="score")]
article_link = [tag.get("href") for tag in soup.find_all(name='a', class_="storylink")]

print(f"{article_text[0]}\n{article_score[0].splip(' ')}\n{article_link[0]}")