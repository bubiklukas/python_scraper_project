from selenium import webdriver
import random

class scraper_bot(object):
    def __init__(self):
        #initialize
        self.path = "C:\Program Files (x86)\chromedriver.exe"
        self.options = webdriver.ChromeOptions()
        self.user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.56 Safari/537.36"
        self.options.add_argument(f'user-agent={self.user_agent}')
        self.options.add_argument('headless')
        self.options.add_argument('window-size=1920x1080')
        self.options.add_argument("disable-gpu")
        self.driver = webdriver.Chrome(self.path, options=self.options)
        self.url = "https://www.idnes.cz/"
        self.driver.get(self.url)
        #lists
        self.h3_list = []
    def get_news(self):
        raw_h3 = self.driver.find_elements_by_xpath('//a/h3')
        for elem in raw_h3:
            self.h3_list.append(elem.text)
        return self.h3_list
    def sample(self, num):
        return random.sample(self.h3_list, num)
    def stop(self):
        self.driver.quit()
bot = scraper_bot()

bot.get_news()
print(bot.sample(4))
bot.stop()