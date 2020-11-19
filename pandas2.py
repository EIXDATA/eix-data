import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('producment_data.csv', usecols=['CLIENT_COUNTRY', 'WIN_NAME', 'VALUE'])

df = pd.DataFrame(data)
'''
# costain = df['WIN_NAME'].str.contains('Costain').value_counts()
country = df['CLIENT_COUNTRY'].value_counts().reset_index()
group = df.groupby('CLIENT_COUNTRY')
# costain2 = df.WIN_NAME.str.contains('Costain')
country.columns = ['country', 'amount']

country.plot(kind='bar', x='country', y='amount')
plt.show()
'''
df = df.dropna()
df['VALUE'] = df['VALUE'].astype(int)
df_filter = df[df['VALUE'] > 100000]

top = df_filter.nlargest(100,'VALUE')

print(top)
