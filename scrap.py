import selenium.webdriver.common.keys as Keys
from selenium import webdriver
import time

path = "/Users/jamssheaton/PycharmProjects/MVP/chromedriver"
driver = webdriver.Chrome(path)
url = "https://ec.europa.eu/eipp/desktop/en/card-view.html#c,projects=+submitDateStr/asc"
driver.get(url)
time.sleep(3)


last_page = driver.find_element_by_id('last-page')
print(last_page.text)

# close Chrome
driver.close()
