def g():
  s = 'inside f()'
  print(s)


'''
def s(qty, item, price):
  print(f'{qty} {item} cost ${price:.2f}')

s(6,'apples',1.67)

s(item='apple', price=2.34, qty=4)
'''
# def f(qty=6, item='bananas', price=1.74):
#  print(f'{qty} {item} cost ${price:.2f}')

'''

def a(B=None):
  if B is None:
    my_list=[]
    my_list.append('###')
  print(id(my_list))
  print(my_list)
  return my_list
'''
'''
def f(x):
  x['pete'] = 45


my_dict = {'james' : 32, 'pete' : 40, 'john' : 54}

f(my_dict)
print(my_dict)
'''

'''
def double(x):
  return x * 2
x = 5
v = double(x)
'''
'''
def double_list(x):
  i = 0
  while i < len(x):
    x[i] *= 2
    i += 1

a = [5,2,3,12,5]
double_list(a)
print(a)
'''
'''
def double_list(x):
  r = []
  for i in x:
    r.append(i * 2)
  return r

a =[1,2,3,4,5]

a = double_list(a)

print(a)
'''
'''
def avg(a):
  total = 0
  for v in a:
    total += v
  return total / len(a)

x = avg([1,4,7,9])
print(x)
'''
'''
def avg(*args):
  total = 0
  for i in args:
    total += i
  return total / len(args)

x = avg(1,2,3,4,5)

print(x)
'''

'''
def avg(*args):
  total = 0
  for x in args:
    if isinstance(x,int):
      total += x
    else:
      pass
      #print('you have a string, which has been removed =', x)
  return total / len(args)

tup = avg(1,2,3,4,5,88,5,6,10,12,'hello')
tup = round(tup,2)
#print(tup)


def f(x,y,z):
  print(f'x = {x}')
  print(f'y = {y}')
  print(f'z = {z}')

t = ('hello','hi','bye')

print(f(*t))
'''
'''
def f(**kwargs):
  print(kwargs)
  print(type(kwargs))
  for key, val in kwargs.items():
    print(key, '->', val)

t = f(hello=1, hi=2, bye=3)
'''
'''
def f(a,b,*args, **kwargs):
  print(f'a = {a}')
  print(f'b = {b}')
  print(f'args = {args}')
  print(f'kwargs = {kwargs}')

t = f(1,2,'hello','hi', 'bye', x=100, y=200, z=300)
print(t)
'''
'''
def f(*args):
  for i in args:
    print(i)

s = [1,2,3]
t = (4,5,6)
se = {7,8,9}

t = f(*s, *t, *se)
print(t)
'''
'''
def f(**kwargs):
  for k, v in kwargs.items():
    print(k, '->', v)

d1 = {'a' : 1, 'b' : 2}
d2 = {'x' : 3, 'y' : 4}

f(**d1,**d2)
'''

'''
def concat(*args, prefix='-> ', sep='_'):
  print(f'{prefix}{sep.join(args)}')

concat('hello','hi','bye', sep='/', prefix='xxx ')
'''

'''
def oper(x,y,*, op='+'):
  if op =='+':
    return x + y
  elif op == '-':
    return x - y
  elif op == '/':
    return x / y
  else:
    return None

t = oper(3,4,op='/')
print(t)
'''

'''
def f(x,y,/,z):
  print(f'x: {x}')
  print(f'y: {y}')
  print(f'z: {z}')

f(1,2,z=8)
'''


def f(x, y, /, z, w, *, a, b):
  print(x, y, z, w, a, b)

f(1, 2, z=3, w=4, a=5, b=6)

locals()



def f(win_name):
  list2 = []
  for x in win_name:
    list2.append(x['WIN_NAME'])
  return list(set(list2))

t = f(win_list)
