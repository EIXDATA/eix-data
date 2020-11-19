import untangle

ob = untangle.parse('/Users/jamssheaton/PycharmProjects/MVP/ted_data/20201014_200/483919_2020.xml')
ob2 = untangle.parse('/Users/jamssheaton/PycharmProjects/MVP/ted_data/20201015_201/486830_2020.xml')

doc = ob.TED_EXPORT.FORM_SECTION.F03_2014
doc2 = ob2.TED_EXPORT.FORM_SECTION.F03_2014

print(doc2)


#.AWARDED_CONTRACT.CONTRACTORS.CONTRACTOR.ADDRESS_CONTRACTOR.OFFICIALNAME
