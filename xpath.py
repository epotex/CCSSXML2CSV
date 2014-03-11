from lxml import etree
file = 'xml-in.xml'
tree = etree.parse(file).getroot()
#namespaces={'skos':'http://www.w3.org/2004/02/skos/core#','rdfs':'http://www.w3.org/2000/01/rdf-schema#','gemq':'http://purl.org/gem/qualifiers/','loc':'http://www.loc.gov/loc.terms/relators/','owl':'http://www.w3.org/2002/07/owl#','asn':'http://purl.org/ASN/schema/core/', 'cc':'http://creativecommons.org/ns#','dc':'http://purl.org/dc/elements/1.1/','dcterms':'http://purl.org/dc/terms/','foaf':'http://xmlns.com/foaf/0.1/', 'rdf':'http://www.w3.org/2000/01/rdf-schema#', 'dcterms': 'http://purl.org/dc/terms/'})
#educationLevel = element.xpath('*[local-name()="educationLevel"]')


#Global Vars
grade = "12'}"
Country ='USA'
State = ''
Standard_Pack = 'CCSS'
selectable = ''
Discipline = 'Math'
Grade_Level = 'Fifth'

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
<<<<<<< HEAD
StatementNotation = tree.xpath('.//asn:Statement/asn:statementNotation/text()',  namespaces = tree.nsmap)
About = tree.xpath('.//asn:Statement/@rdf:about',  namespaces = tree.nsmap)
Elements = tree.xpath('//asn:Statement/*', namespaces = tree.nsmap)

child = tree.xpath('child::node()')
for x in child:
    print   x.getparent()


for x in tree:
    print x.xpath('child')
    

        
            


=======
StatementNotation = tree.xpath('.//asn:statementNotation',  namespaces = tree.nsmap)#TEXT
About = tree.findall('asn:Statement', namespaces = tree.nsmap)


# 
# for id in  About:
#         
#         print  value


for id in  About:
    for state in  id:
        if state == "{http://purl.org/ASN/schema/core/}statementNotation":
            print state
        
    # for key,value  in  id.attrib.iteritems():
     #    for x in StatementNotation:
      #       print  x.text, value
         
            
    
>>>>>>> d2462f71dfc88e55424d1e8a100c245f5dc54cd1
#About = tree.findall('.//asn:Statement/rdf:about',  namespaces = tree.nsmap)

#for x in get_xpath_attrib_value_list(StatementNotation):


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
    print Country, ';',    State, ';',    Standard_Pack, ';',    Discipline, ';',    Grade_Level, ';',    GeneralId, ';',    '', ';',    'Selectable', ';',    GeneralName, ';',    GeneralDescription

#Get the ALL entity(beside the General entity)
def get_all_entities():
    #Xpath XML items Vars:
    for element in tree.getchildren():
        for a in element.xpath('.//dcterms:educationLevel',  namespaces = tree.nsmap):
            #===================================================================
            # Statement = element.xpath('asn:Statement',  namespaces = tree.nsmap)
            #===================================================================
            test = get_xpath_attrib_value_list(Subject)
             
            if a.attrib == {'{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource': 'http://purl.org/ASN/scheme/ASNEducationLevel/8'}:
               for a in StatementNotation:
                   if  a.text is not None:
                       print [tree.xpath('*/StatementCode')[0].text, tree.xpath('*/Statement')[0].text, tree.xpath('*/description')[0].text, tree.xpath('*/GradeLevel')[0].text]
                       #yield  Country, ';', State, ';', Standard_Pack, ';', Discipline, ';', Grade_Level, ';', a.text, ';', "", ';', selectable, ';', Description[0].text, ';', Comment



    



id_url_dict ={}
def get_xpath_attrib_value_list(x):
    for a in x:
        id_url_dict[a] = a.attrib
        for value in dict.itervalues():
            yield value       

#===============================================================================
# 
# for id in StatementNotation:
#     print id
#                 
# def get_parent_id():
#     for entity in etree.parse(file).getroot():
#         haschild_list =[]
#         child_id_dict = {}
#         
#         
#===============================================================================
#         for  a in get_xpath_attrib_value_list(Haschild):
#             haschild_list.append(a, a.text)
#             print a
#         for  b in get_xpath_attrib_value_list(Statement):
#             child_id_dict.append(b)
#         for key, in haschild_dict:
#             for z in child_id_dict:
#                 if z == key:
#                     yield z , value
#     for  a in get_xpath_attrib_value_list(Haschild):
#         try:
#             print a
#         except TypeError: 
#             pass

#for x in get_parent_id():
 #   print x
#for entity in etree.parse(file).getroot():
 #   for b in get_xpath_attrib_value_list(IsChildOf):
  #       if  b == a:
   #          print "mach"
#print About

    #print  entity.attrib
#get_parent()




#


id_url_dict ={}
# def get_xpath_attrib_value_list(x):
#     for a in x:
#         id_url_dict[a] = a.attrib
#         for value in dict.itervalues():
#             yield value       

#===============================================================================
# 
# for id in StatementNotation:
#     print id
#                 
# def get_parent_id():
#     for entity in etree.parse(file).getroot():
#         haschild_list =[]
#         child_id_dict = {}
#         
#         
#===============================================================================
#         for  a in get_xpath_attrib_value_list(Haschild):
#             haschild_list.append(a, a.text)
#             print a
#         for  b in get_xpath_attrib_value_list(Statement):
#             child_id_dict.append(b)
#         for key, in haschild_dict:
#             for z in child_id_dict:
#                 if z == key:
#                     yield z , value
#     for  a in get_xpath_attrib_value_list(Haschild):
#         try:
#             print a
#         except TypeError: 
#             pass

#for x in get_parent_id():
 #   print x
#for entity in etree.parse(file).getroot():
 #   for b in get_xpath_attrib_value_list(IsChildOf):
  #       if  b == a:
   #          print "mach"
#print About

    #print  entity.attrib
#get_parent()


#Script:#            
<<<<<<< HEAD
# get_csv_header()
# get_general_entity()    
=======
#get_csv_header()
#get_general_entity()    
>>>>>>> d2462f71dfc88e55424d1e8a100c245f5dc54cd1
#for results in get_all_entities():
 #   print results

