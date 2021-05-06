import random
from selenium import webdriver



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
        self.url = "https://www.idnes.cz/"
        #lists
        self.sample_h3 = []
        self.sample_href = []
        self.h3_list = []
        self.href_list = []
    def run(self):
        print('run')
        self.driver = webdriver.Chrome(self.path, options=self.options)
        self.driver.get(self.url)
    def get_news(self):
        print('get_news')
        raw_h3 = self.driver.find_elements_by_xpath('//a[@class="art-link"]/h3')
        raw_href = self.driver.find_elements_by_class_name('art-link')
        for elem in raw_h3:
            self.h3_list.append(elem.text)
        for elem in raw_href:
            href = elem.get_attribute("href")
            self.href_list.append(href)
        return self.h3_list, self.href_list
    def sample(self, num):
        print('sample')
        for i in range(num):
            random_number = random.randrange(1, int((len(self.h3_list)/4)))
            self.sample_h3.append(self.h3_list[random_number])
            self.sample_href.append(self.href_list[random_number])
            self.h3_list.pop(random_number)
            self.href_list.pop(random_number)
            print(random_number)
        return self.sample_h3, self.sample_href
    def stop(self):
        print('stop')
        self.driver.quit()

