from lxml import etree
file = 'xml-in.xml'
tree = etree.parse(file).getroot()

all = tree.xpath('//asn:Statement[@*]', namespaces = tree.nsmap)

#===============================================================================
# Finctions
#===============================================================================
def get_statment():    
     if StatementNotation == []:
         pass
     else:
         yield StatementNotation

def get_edu_level():
    for a in EDU:
        yield a

#===============================================================================
#Script 
#===============================================================================

for x in all:
    s=''
    URLID = x.xpath('//asn:Statement[@rdf:about]',namespaces = tree.nsmap)
    EDU = x.xpath('.//dcterms:educationLevel [@rdf:resource]',  namespaces = tree.nsmap)
    StatementNotation = x.xpath('./asn:statementNotation/text()',  namespaces = tree.nsmap)
    for s in get_statment():
        pass
    for e in get_edu_level():
        pass
    for ID in URLID:
        pass
            


print  ID.attrib, e.attrib, s   
