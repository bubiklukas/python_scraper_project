from flask import Flask, render_template
import sys
from scraper.main import scraper_bot


app = Flask(__name__)



@app.route("/")
def home():
    sample_h3 = []
    sample_href = []
    return render_template("index.html", titles=sample_h3, links=sample_href, loading="none")

@app.route("/botrun/", methods=['POST'])
def bot_run():
    print("before")
    bot = scraper_bot()
    bot.run()
    bot.get_news()
    bot.sample(4)
    print(bot.sample_h3)
    print(bot.sample_href)
    sample_h3 = bot.sample_h3
    sample_href = bot.sample_href
    bot.stop()
    return render_template("index.html", titles=sample_h3, links=sample_href, loading="none")

if __name__ == "__main__":
    app.run(debug=True)
    
