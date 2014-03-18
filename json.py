import sys
import urllib2
import simplejson
import argparse
import csv
import re
##############




MATHURL ="https://s3.amazonaws.com/asnstaticd2l/data/manifest/D10003FB.json"
ELAURL="https://s3.amazonaws.com/asnstaticd2l/data/manifest/D10003FC.json"#ELA
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--discpline", help="Choose your discpline (Ela or Math)")
parser.add_argument("-g", "--grade", help="Choose your grade level")
args = parser.parse_args()
#discpline = args.discpline 
discpline = "ela"
#gradefilter = args.grade
gradefilter = "6"


EDU_LABEL = 'dcterms_educationLevel'
PREF_LABEL = 'prefLabel'

#CSV Header vars
Country='USA'
State=''
Standard_Package='CCSS'
Discipline = discpline
Parent_Id =''
Selectable = ''
Name = ''
Description =''
################
#Functions:

def get_doc(URL):
    req = urllib2.Request(URL)
    opener = urllib2.build_opener()
    data = opener.open(req)
    return simplejson.load(data)


def comparevalue(entity,val):
        
        for i in entity[EDU_LABEL]:
            #===================================================================
            # x =  i['prefLabel']
            # #print x
            # if x == val:
            #     return True
            # return False
            #===================================================================
            try:
                pref = i['prefLabel']#i.get(PREF_LABEL)
            except AttributeError:
                continue
            if pref == val:
                return True
            return False
             
def select_entities(doc, pref_value):
    entities = []
    for entity in doc:
        if comparevalue(entity, pref_value):
            entities.append(entity)
    return entities

def get_asn_id(urlid):
    if urlid:
        asnid = re.findall("([^\/]+)$", str(urlid))
        return asnid
         
def CCSS_Math():
    #print headr
    print 'Country', ';',   'State', ';',   'Standard Package',  ';',  'Discipline', ';',   'Grade Level', ';',   'Ped Id',  ';',  'Parent Id',   ';', 'Selectable',   ';', 'Name',   ';', 'Description'
    for elem in e:
        #if comparevalue(elem,gradefilter):    
        #print elem['id'],';',,';', ''
        print Country,';', State,';', Standard_Package,';', Discipline,';', Grade_Level,';', general_id(), ';', "   " ';','FALSE',';', elem['text'],';'," "
        for child in elem['children']:
            #if comparevalue(child,gradefilter):
                print Country,';', State,';', Standard_Package,';', Discipline,';', Grade_Level,';', child['asn_statementNotation'].strip(),';', "   ", ';','FALSE',';', child['text'],';',' '
                for grandchild in child['children']:
                    #if comparevalue(grandchild,gradefilter):
                         print Country,';', State,';', Standard_Package,';', Discipline,';', Grade_Level,';',grandchild['asn_statementNotation'].strip(), ';',child['asn_statementNotation'].strip(), ';','TRUE',';', Name,';',grandchild['text']

#===============================================================================
# 
#         #old    
# def CCSS_ELA():
#       print 'Country', ';',   'State', ';',   'Standard Package',  ';',  'Discipline', ';',   'Grade Level', ';',   'Ped Id',  ';',  'Parent Id',   ';', 'Selectable',   ';', 'Name',   ';', 'Description'
#       for elem in e:
#         #print header
#         #if comparevalue(elem,gradefilter):
#         if elem['dcterms_description']['literal']:    
#             print Country,';', State,';', Standard_Package,';', Discipline,';', Grade_Level,';', general_id(), ';', elem['dcterms_description']['literal'], ';','FALSE',';', elem['text'],';'," "
#         else:
#             print Country,';', State,';', Standard_Package,';', Discipline,';', Grade_Level,';', general_id(), ';', " ", ';','FALSE',';', elem['text'],';'," "
#         for child in elem['children']:
#             #if comparevalue(child,gradefilter):
#                 print Country,';', State,';', Standard_Package,';', Discipline,';', Grade_Level,';', " ",';', "   ", ';','FALSE',';', child['text'],';',' '
#                 for grandchild in child['children']:
#                     #if comparevalue(grandchild,gradefilter):
#                     print Country,';', State,';', Standard_Package,';', Discipline,';', Grade_Level,';',grandchild['asn_statementNotation'].strip(), ';', " ", ';','TRUE',';', Name,';',grandchild['text']
#===============================================================================
def CCSS_ELA():
      csv_output('Country', 'State', 'Standard Package', 'Discipline', 'Grade Level', 'Ped Id', 'Parent Id', 'Selectable', 'Name', 'Description')
      for elem in e:
        #print header
        #if comparevalue(elem,gradefilter):
        csv_output(Country, State, Standard_Package, Discipline, grade_name(), get_asn_id(elem['id']),  "CCSS", 'FALSE', elem['text'],None)
        for child in elem['children']:
            #if comparevalue(child,gradefilter):
                csv_output( Country, State, Standard_Package, Discipline, grade_name(), get_asn_id(child['id']), get_asn_id(elem['id']), 'FALSE', child['text'],None)
                for grandchild in child['children']:
                    #if comparevalue(grandchild,gradefilter):
                    csv_output( Country, State, Standard_Package, Discipline, grade_name(),get_asn_id(grandchild['id']),  get_asn_id(child['id']), 'TRUE', grandchild['asn_statementNotation'],grandchild['text'])


                   
def general_id():
    
    return 'Grade'+gradefilter

def grade_name():
    
    if gradefilter =='1':
        return 'FIRST'
    elif gradefilter =='2':
        return 'SECOND'
    elif gradefilter =='3':
        return 'THIRD'
    elif gradefilter =='4':
        return 'FOURTH'
    elif gradefilter =='5':
        return 'FIFTH'
    elif gradefilter =='6':
        return 'SIXTH'
    elif gradefilter =='7':
        return 'SEVENTH'
    elif gradefilter =='8':
        return 'EIGHTH'
    elif gradefilter =='9':
        return 'NINTH'
    elif gradefilter =='10':
        return 'TENTH'
    elif gradefilter =='11':
        return 'ELEVENTH'
    elif gradefilter =='12':
        return 'TWELFTH'
    else:
        return 'KINDERGARTEN'
def csv_output(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    filename = general_id() + '_' + discpline.upper() + '.'+'csv'
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='"', lineterminator='\n', quoting=csv.QUOTE_ALL)
        writer.writerow([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10])
        
    csvfile.close()
if __name__ == '__main__':
    
    if discpline.lower() =="ela":
        doc = get_doc(ELAURL)
        e = select_entities(doc, gradefilter)
        CCSS_ELA()
    elif discpline.lower() == "math":
        doc = get_doc(ELAURL)
        e = select_entities(doc, gradefilter)
        CCSS_Math()
#===============================================================================
# 
# #check that all group levels are coming in
#     doc = get_doc(ELAURL)
#     e = select_entities(doc, gradefilter)
#     for entity in doc:
#         for gl in entity['dcterms_educationLevel']:
#             print gl['prefLabel']
#         
#===============================================================================