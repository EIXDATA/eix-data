import selenium.webdriver.common.keys as Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

path = "/Users/jamssheaton/PycharmProjects/MVP/chromedriver"
driver = webdriver.Chrome(path, options=chrome_options)
url = "https://infrastructure.planninginspectorate.gov.uk/projects/register-of-applications/"
driver.get(url)

print(driver.page_source)

driver.quit()
