from lxml import etree
import csv

file = 'xml-in.xml'
tree = etree.parse(file).getroot()
all = tree.getchildren()#xpath('//asn:Statement[@*]', namespaces = tree.nsmap)
#url http://s3.amazonaws.com/asnstatic/data/rdf/D10003FB.xml
#===============================================================================
# Finctions
#===============================================================================
for x in all:
    UrlId = x.xpath('//asn:Statement[@rdf:about]',namespaces = tree.nsmap)
    Grade = x.xpath('.//dcterms:educationLevel [@rdf:resource]',  namespaces = tree.nsmap)
    StatementNotation = x.xpath('./asn:statementNotation/text()',  namespaces = tree.nsmap)
    Description = x.xpath('//asn:Statement/dcterms:description/text()',  namespaces = tree.nsmap)

def get_statement():
    for item in StatementNotation:
        if item == []:
            pass
        else:
            yield item
def get_description():
    for item in Description:
        if item == []:
            pass
        else:
            yield item    
def get_grade_level():
    for item in Grade:
        if item == []:
            pass
        else:
            yield item.values()
def get_UrlId():
    for item in UrlId:
        if item == []:
            pass
        else:
            yield item.values()
            
def csv_writer():
     with open(r"out.csv", "wb") as csv_file:
         writer = csv.writer(csv_file, delimiter =",",quoting=csv.QUOTE_MINIMAL)
         writer.writerow([ID,level,state,x])

#===============================================================================
#Script 
#===============================================================================
for state in get_statement():
    pass
for level in get_grade_level():
    pass
for ID in get_UrlId():
    pass
for x in get_description():
    pass
       


print ID,level,state,x
    
csv_writer()

               