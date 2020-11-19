import selenium.webdriver.common.keys as Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import pandas as pd

path = "/Users/jamssheaton/PycharmProjects/MVP/chromedriver"
driver = webdriver.Chrome(path)
url = "https://ec.europa.eu/eipp/desktop/en/card-view.html#c,projects=+submitDateStr/asc"
driver.get(url)
time.sleep(5)

search = driver.find_element_by_xpath("//*[@id='project-cost-min']")
search.send_keys('100')
time.sleep(3)
list2 = driver.find_element_by_xpath("//*[@id='search']/div[1]/div/div[2]/div/span[1]/div/button")
list2.click()
time.sleep(3)
list = driver.find_element_by_xpath("//*[@id='search']/div[1]/div/div[2]/div/span[1]/div/ul/li[6]/a/label/input")
list.click()
time.sleep(3)
button = driver.find_element_by_xpath("//*[@id='search_button']")
button.click()
time.sleep(3)
driver.quit()
