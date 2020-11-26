import pandas as pd


cpv = pd.read_csv('./DATA/CPV.csv')
psc = pd.read_csv('./DATA/PSC_Data_October_2020.csv')
psc = pd.DataFrame(psc)
psc = psc[['PSC CODE', 'PRODUCT AND SERVICE CODE NAME']]
psc = psc.rename(columns={'PSC CODE': 'PSC_CODE', 'PRODUCT AND SERVICE CODE NAME' : 'NAME'})
cpv = pd.DataFrame(cpv)


name = psc['NAME'].tolist()
des = cpv['EN'].tolist()
