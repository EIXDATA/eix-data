import collections as co
import array as arr
import requests as requests
import json

#a = ['a','b','c','d','e','f']
#d = co.deque(a)
#d.appendleft('python')
#d.popleft()

#d = {2 : "pete", 3 : 'john'}
#a1 = co.ChainMap(c,d)
#print(a1)

#a = (1,1,1,2,2,2,3,4,5,6,6,6,7,7,8,8,9)
#b = co.Counter(a)
#print(b)
#print(list(b.elements()))
#print(list(b.most_common()))
#sub = { 6:1}
#print(b.subtract(sub))
#print(b.most_common())

#d = co.OrderedDict()
#d[1] = 'j'
#d[2] = 'a'
#d[3] = 'm'
#d[4] = 'e'
#d[5] = 's'
#print(d)
#d[1] = 'L'
#print(d)

#d = co.defaultdict(int)
#d[1] = 'james'
#d[2] = 'john'
#print(d)
#a = arr.array('i',[1,2,3,4,5,6,7,8,9,10,11])

#temp=0
#while temp<len(a):
#  print(a[temp])
#  temp=temp+1

responses = list() # stores responses for postal codes
postcodes = ['P0L1B0','P5A3P1', 'P5A3P2', 'P5A3P3', 'P5A3P4', 'P5A3P5']

for postcode in postcodes:
   rr = requests.get('https://represent.opennorth.ca/postcodes/{}'.format(postcode))
   data=json.loads(rr.text)
   responses.append(data)
   print(rr)

with open('rr.json', 'w') as json_file:
  json.dump(responses, json_file)
