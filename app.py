from flask import Flask, render_template
from scraper import scrape_wired_rss

app = Flask(__name__)

@app.route('/')
def home():
    articles = scrape_wired_rss()
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
