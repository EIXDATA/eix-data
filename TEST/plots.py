import matplotlib.pyplot as plt
import numpy as np


'''
# scatter plots exmaple
data = {
  'a' : np.arange(50),
  'c' : np.random.randint(0,50,50),
  'd' : np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.rand(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter( 'a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
'''

'''
names = ['group_a', 'group_b', 'group_c']
values = [1, 50, 500]

plt.figure(figsize=(10, 3))
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('different plots for the same data')
plt.show()
'''

'''
# line style settings
x = 20
y = 30
data = [1,2,3,4,5]
a = plt.plot(data, '--')
plt.setp(a, color='r', lw = '2',)
plt.show()
'''

np.random.seed(444)
