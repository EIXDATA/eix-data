import selenium.webdriver.common.keys as Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

path = "/Users/jamssheaton/PycharmProjects/MVP/chromedriver"
driver = webdriver.Chrome(path)
url = "https://ec.europa.eu/eipp/desktop/en/card-view.html#c,projects=+submitDateStr/asc"
driver.get(url)
temp_des = driver.find_elements_by_class_name("card-label-content")
# next = driver.find_element_by_id('pagination-btn-next')
# pages = [*range(0, 5, 1)]
titles = []
descriptions = []
country_list = []
sectors = []
range = range(10)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col-sm-6"))
    )
    # temp_titles = driver.find_elements_by_id("callout-progress-csp")
    # temp_des = driver.find_elements_by_class_name("card-label-content")
    next_address = driver.find_element_by_id('pagination-btn-next')

    for next2 in range:
      next_address.click()
      temp_titles = driver.find_elements_by_id("callout-progress-csp")
      temp_des = driver.find_elements_by_class_name("card-label-content")
      country_temp = driver.find_elements_by_class_name('card-label-short-info')
      temp_sectors = driver.find_elements_by_class_name('card-label-short-description')

      for title in temp_titles:
        titles.append(title.text)

      for description in temp_des:
        descriptions.append(description.text)

      for country in country_temp:
        country_list.append(country.text)

      for sector in temp_sectors:
        sectors.append(sector.text)

finally:
  print(titles)
  driver.quit()

#aip = list(zip(titles,descriptions,country_list,sectors))
#df = pd.DataFrame(zip, columns=['title', 'descriptions','country','sectors'])
#print(df)
