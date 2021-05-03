from selenium import webdriver
import random
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
URL = "https://www.idnes.cz/"
driver.get(URL)

#get_news
def get_news():
    global list
    list = []
    all_h3 = driver.find_elements_by_xpath('//a/h3')
    for h3 in all_h3:
        list.append(h3.text)
    return list

get_news()
#github_edit
print(random.sample(list, 4))

driver.quit()
