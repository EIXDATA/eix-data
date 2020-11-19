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

titles = []
descriptions = []
country_list = []
country_list2 = []
sectors = []
links_list = []
funded = []
sectors2 = []

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "col-sm-6"))
    )
    # temp_titles = driver.find_elements_by_id("callout-progress-csp")
    # temp_des = driver.find_elements_by_class_name("card-label-content")
    next_address = driver.find_element_by_id('pagination-btn-next')
    temp_last_page = driver.find_element_by_id('last-page')
    last_page = int(temp_last_page.text)
    range = range(10)


    for next2 in range:
      next_address.click()
      temp_titles = driver.find_elements_by_id("callout-progress-csp")
      temp_des = driver.find_elements_by_class_name("card-label-content")
      country_temp = driver.find_elements_by_class_name('card-label-short-info')
      temp_sectors = driver.find_elements_by_class_name('card-label-short-description')
      temp_finance = driver.find_elements_by_xpath("//span[@class='card-label-bold card-label-financed']")
      print('200')

      for title in temp_titles:
        titles.append(title.text)
        # "driver.find_element_by_link_text('" + title.text + "').get_attribute('href')"
        links = driver.find_element_by_link_text(title.text).get_attribute('href')
        links_list.append(links)

      for description in temp_des:
        descriptions.append(description.text)

      for country in country_temp:
        country_list.append(country.text)

      for sector in temp_sectors:
        sectors.append(sector.text)

      for finance in temp_finance:
        funded.append(finance.text)

finally:
  for x in sectors:
    z = x.replace('\n', ' / ')
    sectors2.append(z)

  for a in country_list:
    b = a.replace('\n', ' / ')
    country_list2.append(b)

driver.quit()

#zip = list(zip(titles,descriptions,country_list2, sectors2 ,links_list, funded))
#df = pd.DataFrame(zip, columns=['title', 'description', 'country', 'sectors', 'link', 'finance'])

#df.to_csv('export.csv', index=False)

#print(df)
