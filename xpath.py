from lxml import etree
file = 'xml-in.xml'
#namespaces={'skos':'http://www.w3.org/2004/02/skos/core#','rdfs':'http://www.w3.org/2000/01/rdf-schema#','gemq':'http://purl.org/gem/qualifiers/','loc':'http://www.loc.gov/loc.terms/relators/','owl':'http://www.w3.org/2002/07/owl#','asn':'http://purl.org/ASN/schema/core/', 'cc':'http://creativecommons.org/ns#','dc':'http://purl.org/dc/elements/1.1/','dcterms':'http://purl.org/dc/terms/','foaf':'http://xmlns.com/foaf/0.1/', 'rdf':'http://www.w3.org/2000/01/rdf-schema#', 'dcterms': 'http://purl.org/dc/terms/'})
#educationLevel = element.xpath('*[local-name()="educationLevel"]')


tree = etree.parse(file).getroot()


#Global Vars
grade = "12'}"
#gradefilter  = "{'{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource': 'http://purl.org/ASN/scheme/ASNEducationLevel/" + grade
   

for element in tree.getchildren():
    #Xpath XML items Vars:
    Statement = element.xpath('asn:Statement',  namespaces = tree.nsmap)
    EducationLevel = element.xpath('.//dcterms:educationLevel',  namespaces = tree.nsmap)
    Subject = element.xpath('.//dcterms:subject ',  namespaces = tree.nsmap)
    Description = element.xpath('.//dcterms:description ',  namespaces = tree.nsmap)
    Haschild = element.xpath('.//gemq:hasChild  ',  namespaces = tree.nsmap)
    Language = element.xpath('.//dcterms:language  ',  namespaces = tree.nsmap)
    IsChildOf = element.xpath('.//gemq:isChildOf ',  namespaces = tree.nsmap)
    AuthorityStatus = element.xpath('.//asn:authorityStatus ',  namespaces = tree.nsmap)
    IndexingStatus = element.xpath('.//asn:indexingStatus ',  namespaces = tree.nsmap)
    IsPartOf = element.xpath('.//dcterms:isPartOf ',  namespaces = tree.nsmap)
    StatementNotation = element.xpath('asn:statementNotation ',  namespaces = tree.nsmap)

  

    for a in element.xpath('.//dcterms:educationLevel',  namespaces = tree.nsmap):
        #print a.attrib
        #print gradefilter
     
        if  a.attrib == {'{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource': 'http://purl.org/ASN/scheme/ASNEducationLevel/10'}:
         
            print Subject[0].attrib, Description[0].text, Language[0].attrib
        #else:
         #   print "no"
    
    
    


   # if element.attrib == greadefilter:
        
    
        

