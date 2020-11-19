import pandas as pd

data = {
  'apples': [3, 2, 0, 1],
  'oranges': [0, 3, 7, 2]
}

df2 = pd.DataFrame(data, index=['james', 'robert', 'lily', 'david'])

# df = pd.read_csv('purchases.csv', index_col=0)

# df = pd.read_json('purchases.json')

print(df2)
