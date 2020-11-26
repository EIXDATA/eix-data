import pprint as pp
from XML.get_files import getListOfFiles, getroot

# NEED TO UPDATE AS PER TESTNS
NMSP = {'ns': 'http://publications.europa.eu/resource/schema/ted/R2.0.9/publication'}
NSNUTS = {'ns': 'http://publications.europa.eu/resource/schema/ted/2016/nuts'}

# NEED TO REPLACE WITH FOR FILTER OF TED FOLDER
#link = '/Users/jamssheaton/PycharmProjects/MVP/ted_data/20201109_218/535158_2020.xml'
#tree = etree.parse(link)

# GET FILES
dirName = '/Users/jamssheaton/PycharmProjects/MVP/ted_data'
allFiles = getListOfFiles(dirName)
allFiles = allFiles[0:2]
roots = getroot(allFiles)

# XPATH REFS
exprText = "//*[local-name() = $name]/text()"
exprCode = "//*[local-name() = $name]/@CODE"
exprValue = "//*[local-name() = $name]/@VALUE"
exprLG = "//*[local-name() = $name]/@LG"

def getNotice(xml):
  obj = dict()

  for item in ['ORIGINAL_CPV', 'ORIGINAL_NUTS']:
    obj[item] = xml.xpath(exprCode, namespaces=NMSP, name=item)

  for nuts in ['PERFORMANCE_NUTS', 'CA_CE_NUTS']:
    obj[nuts] = xml.xpath(exprCode, namespaces=NSNUTS, name=nuts)

  obj['NO_DOC_OJS'] = xml.xpath(exprText, namespaces=NMSP, name='NO_DOC_OJS')
  obj['IA_URL_GENERAL'] = xml.xpath(exprText, namespaces=NMSP, name='IA_URL_GENERAL')
  obj['ISO_COUNTRY'] = xml.xpath(exprValue, namespaces=NMSP, name='ISO_COUNTRY')
  obj['IA_URL_GENERAL'] = xml.xpath(exprText, namespaces=NMSP, name='IA_URL_GENERAL')
  obj['URL'] = xml.xpath(exprText, namespaces=NMSP, name='URI_DOC')[0]
  obj['PROCUREMENT_TOTAL'] = xml.xpath(".//ns:VALUES/* [@TYPE ='PROCUREMENT_TOTAL']/text()", namespaces=NMSP)
  obj['CURRENCY'] = xml.xpath(".//ns:VALUES/ns:VALUE/@CURRENCY", namespaces=NMSP)

  return obj

def getCodif(xml):
  obj = dict()

  for item in ['AA_AUTHORITY_TYPE', 'TD_DOCUMENT_TYPE', 'NC_CONTRACT_NATURE',
               'PR_PROC', 'TY_TYPE_BID', 'MA_MAIN_ACTIVITIES']:
    el = xml.xpath(exprCode, name=item, namespaces=NMSP)
    obj[item] = el

  obj['DS_DATE_DISPATCH'] = xml.xpath(exprText, name='DS_DATE_DISPATCH', namespaces=NMSP)
  obj['DT_DATE_FOR_SUBMISSION'] = xml.xpath(exprText, name='DT_DATE_FOR_SUBMISSION', namespaces=NMSP)

  return obj


def getContract(xml):
  global form
  obj = dict()

  if xml.xpath(".//ns:FORM_SECTION/*/@CATEGORY = 'ORIGINAL'", namespaces=NMSP):
    form = xml.xpath('ns:FORM_SECTION', namespaces=NMSP)[0][0]
  else:
    pass
  for item in ['OFFICIALNAME', 'ADDRESS', 'TOWN', 'POSTAL_CODE', 'E_MAIL']:
    obj[item] = form.xpath(f".//ns:ADDRESS_CONTRACTING_BODY/ns:{item}/text()", namespaces=NMSP)

  return obj


def getObject(xml):
  obj = dict()

  obj['CPV_MAIN'] = xml.xpath('.//ns:CPV_MAIN/ns:CPV_CODE/@CODE', namespaces=NMSP)
  obj['TITLE'] = xml.xpath('.//ns:OBJECT_CONTRACT/ns:TITLE/ns:P/text()', namespaces=NMSP)
  obj['SHORT_DESCR'] = xml.xpath('.//ns:OBJECT_CONTRACT/ns:NUTS/@CODE', namespaces=NSNUTS)

  return obj


# REFERENCE TO TOP OF NS, NEED TO UPDATE AND SEE IMPACT!
TESTNS = {'ns': 'http://publications.europa.eu/resource/schema/ted/R2.0.9/publication',
          'nuts': 'http://publications.europa.eu/resource/schema/ted/2016/nuts'}


def objectDes(xml):

  obj = dict()
  objList = []
  lots = xml.xpath('.//ns:OBJECT_DESCR', namespaces=NMSP)

  for lot in lots:
    obj['LOT_NO'] = lot.xpath('.//ns:LOT_NO/text()', namespaces=NMSP)
    for item in ['TITLE', 'MAIN_SITE', 'SHORT_DESCR']:
      obj[item] = lot.xpath(f'.//ns:{item}/ns:P/text()', namespaces=NMSP)

    obj['CPV_ADDITIONAL'] = lot.xpath('.//ns:CPV_ADDITIONAL/ns:CPV_CODE/@CODE', namespaces=NMSP)
    obj['NUTS'] = lot.xpath('.//nuts:NUTS/@CODE', namespaces=TESTNS)
    obvCopy = obj.copy()
    objList.append(obvCopy)

  return objList


def getAward(xml):
  global awards
  obj = dict()
  objList = []

  if xml.xpath(".//ns:FORM_SECTION/*/@CATEGORY = 'ORIGINAL'", namespaces=NMSP):
    awards = xml.xpath('.//ns:AWARD_CONTRACT', namespaces=NMSP)
  else:
    pass
  obj = dict()
  for award in awards:
    obj['CONTRACT_NO'] = award.xpath('ns:CONTRACT_NO/text()', namespaces=NMSP)
    obj['TITLE'] = award.xpath('ns:TITLE/ns:P/text()', namespaces=NMSP)
    obj['OFFICIALNAME'] = award.xpath('ns:AWARDED_CONTRACT/ns:CONTRACTORS/ns:CONTRACTOR/'
                                  'ns:ADDRESS_CONTRACTOR/ns:OFFICIALNAME/text()', namespaces=NMSP)
    obj['ADDRESS'] = award.xpath('ns:AWARDED_CONTRACT/ns:CONTRACTORS/ns:CONTRACTOR/'
                             'ns:ADDRESS_CONTRACTOR/ns:ADDRESS/text()', namespaces=NMSP)
    obj['TOWN'] = award.xpath('ns:AWARDED_CONTRACT/ns:CONTRACTORS/ns:CONTRACTOR/'
                          'ns:ADDRESS_CONTRACTOR/ns:TOWN/text()', namespaces=NMSP)
    obj['POSTAL_CODE'] = award.xpath('ns:AWARDED_CONTRACT/ns:CONTRACTORS/ns:CONTRACTOR/'
                                 'ns:ADDRESS_CONTRACTOR/ns:POSTAL_CODE/text()', namespaces=NMSP)
    obj['VAL_TOTAL'] = award.xpath('ns:AWARDED_CONTRACT/ns:VALUES/ns:VAL_TOTAL/text()', namespaces=NMSP)
    obvCopy = obj.copy()
    objList.append(obvCopy)

  return objList

def getComplementary(xml):
  obj = dict()
  com = xml.xpath('ns:FORM_SECTION', namespaces=NMSP)[0][0]

  for item in ['OFFICIALNAME', 'TOWN']:
    obj[item] = com.xpath(f'ns:COMPLEMENTARY_INFO//*/ns:{item}/text()', namespaces=NMSP)

    obj['REVIEW_PROCEDURE'] = com.xpath(f'ns:COMPLEMENTARY_INFO/ns:REVIEW_PROCEDURE/ns:P/text()', namespaces=NMSP)

    return obj


def getCoded(xml):
  obj = dict()

  obj['NOTICE_DATA'] = getNotice(xml)
  obj['CODIF_DATA'] = getCodif(xml)

  return obj


def contract(xml):
  obj = dict()
  obj['CONTRACTOR'] = getContract(xml)
  obj['OBJECT'] = getObject(xml)
  obj['LOTS'] = objectDes(xml)

  return obj


def getTED(xml):
  obj = dict()

  obj['CODED'] = getCoded(xml)
  obj['NOTICE'] = contract(xml)
  obj['AWARD'] = getAward(xml)

  return obj

'''
for w in roots:
  pp.pprint(objectDes(w))

for link in roots:
  print(getNotice(link))
'''
