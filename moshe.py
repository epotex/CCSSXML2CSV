from lxml import etree
import csv

file = 'xml-in.xml'
tree = etree.parse(file).getroot()
all = tree #xpath('//asn:Statement[@*]', namespaces = tree.nsmap)
#url http://s3.amazonaws.com/asnstatic/data/rdf/D10003FB.xml
#===============================================================================
# Finctions
#===============================================================================
for x in all:
 
    UrlId = x.xpath('.//asn:Statement[@rdf:about]',namespaces = tree.nsmap)
    Grade = x.xpath('.//dcterms:educationLevel [@rdf:resource]',  namespaces = tree.nsmap)
    StatementNotation = x.xpath('./asn:statementNotation/text()',  namespaces = tree.nsmap)
    Description = x.xpath('//asn:Statement/dcterms:description/text()',  namespaces = tree.nsmap)
    Parent = x.xpath('//asn:Statement/gemq:isChildOf ',  namespaces = tree.nsmap)
   
def get_statement():
    for item in StatementNotation:
        if item == []:
            pass
        else:
            yield item
def get_Parent():
    for item in Parent:
        if item == []:
            pass
        else:
            yield item.values()

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
# for parent in get_Parent():
#         for parentstate in get_statement():
#             print parentstate
#            
#     
    #print child,ID  

print level,state,x
    
#csv_writer()

               