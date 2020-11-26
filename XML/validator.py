import re
import os
import pprint as pp
from lxml import etree
import pandas as pd
from XML.xml_doc_4 import getTED, getCodif, getObject, getNotice, getAward, getCoded, roots, objectDes
from voluptuous import Schema, Required, Optional, Length, All, Any
import datetime as dt
import json
from ast import literal_eval

link = '/Users/jamssheaton/PycharmProjects/MVP/ted_data/20201109_218/535158_2020.xml'
tree = etree.parse(link)

is_country = pd.read_csv('/Users/jamssheaton/PycharmProjects/MVP/Lookups/ISO_COUNTRY.csv',
                         dtype='str', encoding='latin', keep_default_na=False)
aa = pd.read_csv('/Users/jamssheaton/PycharmProjects/MVP/Lookups/AA_AUTHORITY_TYPE.csv', dtype='str')
ac = pd.read_csv('/Users/jamssheaton/PycharmProjects/MVP/Lookups/AC_AWARD_CRIT.csv', dtype='str')
cpv = pd.read_csv('/Users/jamssheaton/PycharmProjects/MVP/Lookups/CPV.csv', dtype='str')
ma = pd.read_csv('/Users/jamssheaton/PycharmProjects/MVP/Lookups/MA_MAIN_ACTIVITY.csv', dtype='str')
nc = pd.read_csv('/Users/jamssheaton/PycharmProjects/MVP/Lookups/NC_CONTRACT_NATURE.csv', dtype='str')
pr = pd.read_csv('/Users/jamssheaton/PycharmProjects/MVP/Lookups/PR_PROC.csv', dtype='str')
rp = pd.read_csv('/Users/jamssheaton/PycharmProjects/MVP/Lookups/RP_REGULATION.csv', dtype='str')
td = pd.read_csv('/Users/jamssheaton/PycharmProjects/MVP/Lookups/TD_DOCUMENT_TYPE.csv', dtype='str')
ry = pd.read_csv('/Users/jamssheaton/PycharmProjects/MVP/Lookups/TY_TYPE_BID.csv', dtype='str')

# Allowed Currencies
'''currencies = ['EUR', 'BGN', 'CHF', 'USD', 'HRK', 'CZK', 'DKK', 'HUF', 'SEK',
              'NOK', 'LTL', 'TRY', 'PLN', 'MKD', 'RON', 'JPY', 'ISK', 'SKK',
              'LVL', 'GBP', 'MTL', 'CYP', 'EEK']'''

def string(value):
  if not value:
    #value = value.replace('[]', 'NULL')
    value = None
  else:
    if len(value) > 1:
      pass
    else:
      value = str(value)
      value = value.replace('[', '')
      value = value.replace(']', '')
      value = value.replace("'", '')
  return value

def numbers(value):
  global x
  for x in value:
    if not value:
      value = None
    else:
      x = float(x)
      x = int(x)
  return x

def date(value):
  if not value:
    value = None
  else:
    value = str(value)
    c = value.replace('[', '').replace(']', '').replace("'",'')
    value = dt.datetime.strptime(c, '%Y%m%d')
  return value

schema = Schema({'CODED' : {'CODIF_DATA' :
  {

      Required('AA_AUTHORITY_TYPE') : string,
      Required('DT_DATE_FOR_SUBMISSION') : string,
      Required('MA_MAIN_ACTIVITIES') : string,
      Required('NC_CONTRACT_NATURE') : string,
      Required('PR_PROC') : string,
      Required('TD_DOCUMENT_TYPE') : string,
      Required('TY_TYPE_BID') : string,
      Required('DS_DATE_DISPATCH') : date,

    },

  'NOTICE_DATA' : {
    Required('IA_URL_GENERAL') : string,
    Optional('ORIGINAL_CPV') : string,
    Optional('ORIGINAL_NUTS'): string,
    Required('PROCUREMENT_TOTAL'): numbers,
    Required('PERFORMANCE_NUTS'): string,
    Required('CA_CE_NUTS'): string,
    Required('NO_DOC_OJS'): string,
    Required('ISO_COUNTRY'): All(string, Length(max=2)),
    Required('URL') : string,
    Required('CURRENCY') : string}

  },
  'NOTICE' : {'CONTRACTOR': {
    Optional('ADDRESS'): string,
    Optional('E_MAIL'): string,
    Optional('OFFICIALNAME'): string,
    Optional('POSTAL_CODE'): string,
    Optional('TOWN'): string,
  },
    'LOTS' : [{
      Optional('CPV_ADDITIONAL') : string,
      Optional('LOT_NO') : string,
      Optional('MAIN_SITE'): string,
      Optional('NUTS'): string,
      Optional('SHORT_DESCR'): string,
      Optional('TITLE'): string,
    }],
    'OBJECT': {
      Optional('CPV_MAIN'): string,
      Optional('SHORT_DESCR'): string,
      Optional('TITLE'): string,
    }
  },
  Optional('AWARD') : [{
    Optional('ADDRESS'): string,
    Optional('CONTRACT_NO'): string,
    Optional('OFFICIALNAME'): string,
    Optional('POSTAL_CODE'): string,
    Optional('TITLE'): string,
    Optional('TOWN'): string,
    Optional('VAL_TOTAL'): numbers,
      }]
},
  extra=True)
z = getTED(tree)
z = schema(z)
pp.pprint(z)

'''
for link in roots:
  z = getTED(link)
  z = schema(z)
'''
