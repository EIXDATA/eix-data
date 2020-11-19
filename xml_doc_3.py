import untangle
import  os
import pandas as pd
from xml.dom import minidom
import xml.etree.ElementTree as ET
from collections import Counter

#for name in current_list:
#  ob = untangle.parse(f'/Users/jamssheaton/PycharmProjects/MVP/ted_data/20201001_191/{name}')
#  v = ob.TED_EXPORT['DOC_ID']
#  print(v)
#mydoc = minidom.parse('/Users/jamssheaton/PycharmProjects/MVP/ted_data/20201002_192/460793_2020.xml')
#items = mydoc.getElementsByTagName('F03_2014')
#print(items[0].attributes['FORM'].value)

dirName = '/Users/jamssheaton/PycharmProjects/MVP/ted_data'
namespace = {'ns': 'http://publications.europa.eu/resource/schema/ted/R2.0.9/publication'}


def getListOfFiles (dirName):
  listOfFiles = os.listdir(dirName)
  allFiles = list()
  listOfFiles.pop(2)
  for entry in listOfFiles:
    fullpath = os.path.join(dirName, entry)
    if os.path.isdir(fullpath):
      allFiles = allFiles + getListOfFiles(fullpath)
    else:
      allFiles.append(fullpath)
  return allFiles


x = getListOfFiles(dirName)


x = x[0:1000]

def getroot (r):
  root = []
  for file in r:
    if file.endswith('.xml'):
      tree = ET.parse(file)
      rootTemp = tree.getroot()
      root.append(rootTemp)
  return root


links = getroot(x)


notice = []
other = []
full = []
F02 = []
F03 = []

def sorter(links):
  for link in links:
    forms = link.find('./ns:FORM_SECTION/', namespace)
    document = link.find('.')
    if forms is not None:
      if len(forms) != 0:
        form = forms.attrib['FORM']
        full.append(document)
        if form == 'F03':
          F03.append(document)
        elif form == 'F02':
          F02.append(document)
        elif form == 'f14':
          pass
        elif form == 'F06':
          pass
        elif form == 'F20':
          pass
        elif form == 'F05':
          pass
        elif form == 'F01':
          pass
        elif form == 'F15':
          pass
        elif form == 'F21':
          pass
        elif form == 'T01':
          pass
        elif form == 'F08':
          pass
        elif form == 'F12':
          pass
        elif form == 'F24':
          pass
        elif form == 'F13':
          pass
        elif form == 'F07':
          pass
        elif form == 'F25':
          pass
        elif form == 'F04':
          pass
        elif form == 'F24':
          pass
        else:
          pass
      else:
        notice.append(document)
    else:
      other.append(document)


sorter(links)

for x in full:
  forms3 = x.find('./ns:FORM_SECTION/', namespace)
  docid = x.find('.').get('DOC_ID')
  test = forms3.tag
  test = test[70:80]
  test2 = x.findall('./ns:CODED_DATA_SECTION/', namespace)
  print(len(test2))

'''
for link in links:
  docid = link.find('.').get('DOC_ID')
  forms = link.find('./ns:FORM_SECTION/', namespace)
  document = link.find('.')
  if forms is not None:
    if len(forms) != 0:
      pass
    else:
      notice.append(document)
  else:
    other.append(document)
'''
