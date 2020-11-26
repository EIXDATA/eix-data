from pymongo import MongoClient
from lxml import etree
import pprint as pp
from XML.xml_doc_4 import getTED, roots, getCoded, allFiles
from XML.validator import schema

#link = '/Users/jamssheaton/PycharmProjects/MVP/ted_data/20201109_218/535158_2020.xml'
#tree2 = etree.parse(link)
#x = getTED(tree2)

# mongo client
client = MongoClient('localhost', 27017)
db = client.EIX

# MondoDB insert one
posts = db.TED_XML
#post_data = z
#result = posts.insert_many(post_data)

for link in roots:
  z = getTED(link)
  z = schema(z)
  result = posts.insert_one(z)

