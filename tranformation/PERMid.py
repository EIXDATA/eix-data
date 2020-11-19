from pymongo import MongoClient
import pandas as pd
import requests
import time

client = MongoClient('localhost', 27017)
db = client.EIX
posts = db.collection_2
hello = posts.find_one({'WIN_TOWN' : 'GREENWOOD'})
win_name = posts.find({'WIN_TOWN' : 'GREENWOOD'})
links = []


def convert(con):
  return list(set(con))

for x in win_name:
  x = x['WIN_NAME']
  link = 'https://api-eit.refinitiv.com/permid/search?q=' + x + '&access-token=921C3ay3X01WYghPSWasWRqinJgLBs4t&num=1'
  links.append(link)

links = convert(links)

for url in links:
  url2 = requests.get('https://api-eit.refinitiv.com/permid/search?q=' + url + '&access-token=921C3ay3X01WYghPSWasWRqinJgLBs4t&num=1')
  print(url2.status_code)
  print(url2.url)
