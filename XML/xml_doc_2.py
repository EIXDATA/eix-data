import untangle
import  os
import pandas as pd
dirName = '/Users/jamssheaton/PycharmProjects/MVP/ted_data'

#for name in current_list:
#  ob = untangle.parse(f'/Users/jamssheaton/PycharmProjects/MVP/ted_data/20201001_191/{name}')
#  v = ob.TED_EXPORT['DOC_ID']
#  print(v)

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

x = x[0:500]
two = []
three = []
f02 = []
f05 = []
f21 = []
con_def = []
f06 = []
f03 = []
award_def = []
f21 = []
noaward = []
award = []
other = []
for name in x:
  ob = untangle.parse(name)
  doc2 = ob.TED_EXPORT['DOC_ID']
  docId = ob.TED_EXPORT.CODED_DATA_SECTION.CODIF_DATA.TD_DOCUMENT_TYPE['CODE']
  form = ob.TED_EXPORT.FORM_SECTION

  if docId == '7':  # awards
    if hasattr(form, 'F06_2014'):
      f06.append(doc2)
    elif hasattr(form, 'F03_2014'):
      f03.append(doc2)
    elif hasattr(form, 'CONTRACT_AWARD_DEFENCE'):
      award_def.append(doc2)
    elif hasattr(form, 'F21_2014'):
      f21.append(doc2)
    else:
      pass

  elif docId == '3':  # contracts
    if hasattr(form, 'F02_2014'):
      f02.append(doc2)
    elif hasattr(form, 'F05_2014'):
      f05.append(doc2)
    elif hasattr(form, 'F21_2014'):
      f21.append(doc2)
    elif hasattr(form, 'CONTRACT_DEFENCE'):
      con_def.append(doc2)
    else:
      pass
  else:
    other.append(doc2)

print(f'total F06 {len(f06)}')
print(f'Total F03 {len(f03)}')
print(f'Total defence award {len(award_def)}')
print(f'Total f21 {len(f21)}')
print(f'Total f02 {len(f02)}')
print(f'Total f05 {len(f05)}')
print(f'Total f21 {len(f21)}')
print(f'Total contract defence {len(con_def)}')
print(f'Total other {len(other)}')
