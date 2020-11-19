from lxml import etree
import pprint as pp

# NEED TO UPDATE AS PER TESTNS
NMSP = {'ns': 'http://publications.europa.eu/resource/schema/ted/R2.0.9/publication'}
NSNUTS = {'ns': 'http://publications.europa.eu/resource/schema/ted/2016/nuts'}

# NEED TO REPLACE WITH FOR FILTER OF TED FOLDER
link = '/Users/jamssheaton/PycharmProjects/MVP/ted_data/20201109_218/535158_2020.xml'
tree = etree.parse(link)

# XPATH REFS
exprText = "//*[local-name() = $name]/text()"
exprCode = "//*[local-name() = $name]/@CODE"
exprValue = "//*[local-name() = $name]/@VALUE"
exprLG = "//*[local-name() = $name]/@LG"

r = tree.xpath('ns:CODED_DATA_SECTION/ns:CODIF_DATA', namespaces=NMSP)
value = tree.xpath(".//ns:VALUES/* [@TYPE ='PROCUREMENT_TOTAL']", namespaces=NMSP)
currency = tree.xpath(".//ns:VALUES/* [@TYPE ='PROCUREMENT_TOTAL']", namespaces=NMSP)[0]

a = tree.xpath('.', namespaces=NMSP)


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

  currency = xml.xpath(".//ns:VALUES/*", namespaces=NMSP)[0]
  currency = currency.attrib['CURRENCY']
  obj['CURRENCY'] = currency

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
  obj = dict()

  form = xml.xpath('ns:FORM_SECTION', namespaces=NMSP)[0][0]

  if form.xpath("name(*) = 'OTH_NOT'"):
    obj['OTH_NOT'] = ['YES']
    return obj
  obj['OTH_NOT'] = ['NO']

  contract = form.xpath("*/*")[0]
  obj['OFFICALNAME'] = contract.xpath(exprText, namespaces=NMSP, name='OFFICIALNAME')[0]
  obj['ADDRESS'] = contract.xpath(exprText, namespaces=NMSP, name='ADDRESS')[0]
  obj['TOWN'] = contract.xpath(exprText, namespaces=NMSP, name='TOWN')[0]
  obj['POSTAL_CODE'] = contract.xpath(exprText, namespaces=NMSP, name='POSTAL_CODE')[0]
  obj['E_MAIL'] = contract.xpath(exprText, namespaces=NMSP, name='E_MAIL')[0]

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
  # NEED TO GET OBJECT_DESCR ITEM NUMBER, AS NOT ALL
  # OBJECTS HAVE A LOT NUMBER

  form = xml.xpath('ns:FORM_SECTION', namespaces=NMSP)[0][0]
  obj = dict()
  for item in ['LOT_NO']:
    obj[item] = form.xpath(f'.//ns:OBJECT_DESCR/ns:{item}/text()', namespaces=NMSP)

  for item in ['TITLE', 'MAIN_SITE', 'SHORT_DESCR']:
    obj[item] = form.xpath(f'.//ns:OBJECT_DESCR/ns:{item}/ns:P/text()', namespaces=NMSP)

  obj['CPV_ADDITIONAL'] = form.xpath('.//ns:OBJECT_DESCR/ns:CPV_ADDITIONAL/ns:CPV_CODE/@CODE', namespaces=NMSP)
  obj['NUTS'] = form.xpath('.//ns:OBJECT_DESCR/nuts:NUTS/@CODE', namespaces=TESTNS)

  return obj

def getAward(xml):
  obj = dict()
  award = xml.xpath('ns:FORM_SECTION', namespaces=NMSP)[0][0]

  obj['CONTRACT_NO'] = award.xpath('ns:AWARD_CONTRACT/ns:CONTRACT_NO/text()', namespaces=NMSP)
  obj['TITLE'] = award.xpath('ns:AWARD_CONTRACT/ns:TITLE/ns:P/text()', namespaces=NMSP)
  obj['TITLE'] = award.xpath('ns:AWARD_CONTRACT/ns:TITLE/ns:P/text()', namespaces=NMSP)

  for item in ['OFFICIALNAME','ADDRESS','TOWN', 'POSTAL_CODE']:
    obj[item] = award.xpath(f'.//ns:AWARD_CONTRACT//*/ns:{item}/text()', namespaces=NMSP)

  obj['VAL_TOTAL'] = award.xpath('.//ns:AWARD_CONTRACT//*/ns:VAL_TOTAL/text()', namespaces=NMSP)

  return obj


def getComplementary(xml):
  obj = dict()
  com = xml.xpath('ns:FORM_SECTION', namespaces=NMSP)[0][0]

  for item in ['OFFICIALNAME','TOWN']:
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
  obj['COMPLEMENTARY_INFO'] = getComplementary(xml)

  return obj

z = getTED(tree)
pp.pprint(z)

#eeeeebn
