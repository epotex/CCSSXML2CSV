from lxml import etree
file = 'xml-in.xml'
#namespaces={'skos':'http://www.w3.org/2004/02/skos/core#','rdfs':'http://www.w3.org/2000/01/rdf-schema#','gemq':'http://purl.org/gem/qualifiers/','loc':'http://www.loc.gov/loc.terms/relators/','owl':'http://www.w3.org/2002/07/owl#','asn':'http://purl.org/ASN/schema/core/', 'cc':'http://creativecommons.org/ns#','dc':'http://purl.org/dc/elements/1.1/','dcterms':'http://purl.org/dc/terms/','foaf':'http://xmlns.com/foaf/0.1/', 'rdf':'http://www.w3.org/2000/01/rdf-schema#', 'dcterms': 'http://purl.org/dc/terms/'})
#educationLevel = element.xpath('*[local-name()="educationLevel"]')
tree = etree.parse(file).getroot()
def get_xpath_attrib_value_list(x):
    for a in x:
        dict = a.attrib
        for value in dict.itervalues():
            yield value

#Global Vars
grade = "12'}"
Country ='USA'
State = ''
Standard_Pack = 'CCSS'
selectable = ''
Discipline = 'Math'
Grade_Level = '5'
#gradefilter  = "{'{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource': 'http://purl.org/ASN/scheme/ASNEducationLevel/" + grade
GeneralDescription =  tree.findall('.//dcterms:description', namespaces = tree.nsmap)[0].text
GeneralId =  tree.findall('.//asn:jurisdiction', namespaces = tree.nsmap)[0].attrib
GeneralName =  tree.findall('.//dc:title', namespaces = tree.nsmap)[0].text
EducationLevel =  tree.findall('.//dcterms:educationLevel', namespaces = tree.nsmap) #list of dict
Statement =  tree.findall('.//asn:Statement', namespaces = tree.nsmap) #list of dict
Subject =  tree.findall('.//dcterms:subject', namespaces = tree.nsmap) #list of dict
Description =  tree.findall('.//dcterms:description', namespaces = tree.nsmap) #TEXT
Comment = tree.findall('.//asn:comment',  namespaces = tree.nsmap)#TEXT
Haschild = tree.findall('.//gemq:hasChild',  namespaces = tree.nsmap)
IsChildOf = tree.findall('.//gemq:isChildOf',  namespaces = tree.nsmap)
IsPartOf = tree.findall('.//dcterms:isPartOf',  namespaces = tree.nsmap)
StatementNotation = tree.findall('.//asn:statementNotation',  namespaces = tree.nsmap)#TEXT

    

#for x in get_xpath_attrib_value_list(StatementNotation):
 #   print x


#Get the Header for the CSV file
def get_csv_header():
    print 'Country', ';',    'State', ';',    'Standard Package', ';',    'Discipline', ';',    'Grade Level', ';',    'Ped Id', ';',    'Parent Id', ';',    'Selectable', ';',    'Name', ';',    'Description'
#Get Value from a list of dict
#Get Value from a dict
def get_xpath_attrib_value_dict(x):
    for key, value in x.iteritems():
        print  value

#Get the General entity
def get_general_entity():
    #Xpath XML items Vars:
    pass
    #print Country, ';',    State, ';',    Standard_Pack, ';',    Discipline, ';',    Grade_Level, ';',    GeneralId, ';',    '', ';',    'Selectable', ';',    GeneralName, ';',    GeneralDescription
#Get the ALL entity(beside the General entity)
def get_all_entitys():
    #Xpath XML items Vars:
    for element in tree.getchildren():
        for a in element.xpath('.//dcterms:educationLevel',  namespaces = tree.nsmap):
            Statement = element.xpath('asn:Statement',  namespaces = tree.nsmap)
            #EducationLevel = element.xpath('.//dcterms:educationLevel',  namespaces = tree.nsmap) #dict
            edu =  tree.findall('.//dcterms:educationLevel', namespaces = tree.nsmap)#list of dict
            #Subject = element.xpath('.//dcterms:subject ',  namespaces = tree.nsmap)
            Description = element.xpath('.//dcterms:description ',  namespaces = tree.nsmap)
            Comment = element.xpath('.//asn:comment ',  namespaces = tree.nsmap)
            Haschild = element.xpath('.//gemq:hasChild  ',  namespaces = tree.nsmap)
            Language = element.xpath('.//dcterms:language  ',  namespaces = tree.nsmap)
            IsChildOf = element.xpath('.//gemq:isChildOf ',  namespaces = tree.nsmap)
            AuthorityStatus = element.xpath('.//asn:authorityStatus ',  namespaces = tree.nsmap)
            IndexingStatus = element.xpath('.//asn:indexingStatus ',  namespaces = tree.nsmap)
            IsPartOf = element.xpath('.//dcterms:isPartOf ',  namespaces = tree.nsmap)
            StatementNotation = element.xpath('.//asn:statementNotation ',  namespaces = tree.nsmap)
            GeneralNode = element.xpath('//asn:StandardDocument', namespaces = tree.nsmap)  
            if a.attrib == {'{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource': 'http://purl.org/ASN/scheme/ASNEducationLevel/8'}:
               for a in StatementNotation:
                   if  a.text is not None:
                       yield Country, ';', State, ';', Standard_Pack, ';', get_xpath_attrib_value_list(Subject), ';', EducationLevel[0].attrib, ';', a.text, ';', IsChildOf[0].attrib, ';', selectable, ';', Description[0].text, ';', Comment


#Script:#            
#get_csv_header()
#get_general_entity()    
    
for a in get_all_entitys():
    print a
