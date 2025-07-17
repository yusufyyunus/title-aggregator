import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_wired_rss():
    url = "https://www.wired.com/feed/rss"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")

    articles = []

    for item in soup.find_all('item'):
        title = item.title.text
        link = item.link.text
        pub_date = datetime.strptime(item.pubDate.text, "%a, %d %b %Y %H:%M:%S %z")

        if pub_date >= datetime(2022, 1, 1, tzinfo=pub_date.tzinfo):
            articles.append({
                'title': title,
                'link': link,
                'date': pub_date
            })

    articles.sort(key=lambda x: x['date'], reverse=True)
    return articles
