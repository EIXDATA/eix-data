from pymongo import MongoClient
import pandas as pd
from mongoengine import *
import datetime
import pprint as pp


# mongo client
client = MongoClient('localhost', 27017)
db = client.EIX
col = db.TED_XML
#results = col.find_one({"CODED": {"NOTICE_DATA": {"ISO_COUNTRY": "BG"}}})

#for doc in col.find({'CODED': {'CODIF_DATA': {'TD_DOCUMENT_TYPE': '7'}}}):
#  pp.pprint(doc)

for doc in col.find():
  doc = doc['CODED']['NOTICE_DATA']['ISO_COUNTRY']
  print(doc)
