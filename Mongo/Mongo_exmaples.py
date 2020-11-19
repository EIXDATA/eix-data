from pymongo import MongoClient
import pandas as pd
from mongoengine import *
import datetime

'''
# mongo client
client = MongoClient('localhost', 27017)

db = client.EIX

# MondoDB insert one

posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
'''
'''
# insert many posts
posts = db.posts
post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}
new_result = posts.insert_many([post_1, post_2, post_3])
print('Multiple posts: {0}'.format(new_result.inserted_ids))
'''

# find documents
client = MongoClient('localhost', 27017)
db = client.EIX
posts = db.collection_2
hello = posts.find_one({'WIN_TOWN' : 'GREENWOOD'})
findlist = posts.find({'WIN_TOWN' : 'GREENWOOD'})

df = pd.DataFrame(findlist)
print(df)

'''
#object Mongo
connect('mongoengine_test', host='localhost', port= 27017)

class post (Document):
  title = StringField(required=True, max_length=200)
  content = StringField(required=True)
  author = StringField(required=True, max_length=50)
  publish = DateTimeField(default=datetime.datetime.now())
  test = BooleanField()

post_1 = post(
  title = 'sample post',
  content= 'something fun',
  author= 'James',
  test= True
)
post_1.save()
'''
