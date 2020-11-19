from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns

header = ({'User-Agent':
             'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

pages = ['1','2','3','4']
url = 'https://www.gihub.org/resources/data/?currentPage=2'
titles = []
des = []
responce_full = []
link = []

for data in pages:
  url = 'https://www.gihub.org/resources/data/?currentPage=' + data
  responce = get(url, header)
  html_soup = BeautifulSoup(responce.text, 'html.parser')
  temp_titles = html_soup.findAll('div', "article-tile-title")
  temp_des = html_soup.find_all('p', "article-tile-description")
  titles.append(temp_titles)
  des.append(temp_des)
  responce_full.append(responce.text)
  print('responce.url')

responce_link = ''.join(responce_full)
html_link = BeautifulSoup(responce_link, 'html.parser')

for link2 in html_link.findAll('a', {'target': '_blank'}):
  link.append(link2['href'])

title_str = str(titles)
splitter = title_str.split(',')
new_title = []
for x in splitter:
  a = x.replace('<div class="article-tile-title">' , '')
  b = a.replace('</div>','')
  new_title.append(b)

des_srt = str(des)
des_splitter = des_srt.split('</p>')
new_des = []

for z in des_splitter:
  des_temp2 = z.replace('<p class="article-tile-description">', '')
  new_des.append(des_temp2)

#print(len(new_des))
#print(len(link))

zip = list(zip(new_title,new_des,link))
df = pd.DataFrame(zip, columns=['title', 'descriptions', 'link'])
df.to_csv('data.csv', index=True)
