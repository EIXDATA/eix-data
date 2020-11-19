import random as ra
n = 20
to_be_gussed = int(n * ra.random()) + 1
guess = 0
while guess != to_be_gussed:
  guess = int(input('new number :'))
  if guess < n:
    if guess > 0:
      if guess > to_be_gussed:
        print('to large')
      elif guess < to_be_gussed:
        print('to small')
    else:
      print('given up')
      break
  else:
    print("to large must be between 1 - 20")
    else:
    print('woop, i got it')

num = int(input('new number:'))
factor = 1

if num < 0:
  print('must be positive')
elif num == 0:
  print('factor = 1')
else:
  for i in range(1, num + 1):
    factor = factor*i
print(factor)
print(i)

