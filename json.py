import sys
import urllib2
import simplejson
import argparse
import csv
import re
##############

MATHURL ="https://s3.amazonaws.com/asnstaticd2l/data/manifest/D10003FB.json"
ELAURL="https://s3.amazonaws.com/asnstaticd2l/data/manifest/D10003FC.json"#ELA

#parser = argparse.ArgumentParser()
#parser.add_argument("-d", "--discpline", help="Choose your discpline (Ela or Math)")
#parser.add_argument("-g", "--grade", help="Choose your grade level")
#args = parser.parse_args()
#discpline = args.discpline
discpline = "ela"
#gradefilter = args.grade
#gradefilter = "6"


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

entities = []

def get_doc(URL):
    req = urllib2.Request(URL)
    opener = urllib2.build_opener()
    data = opener.open(req)
    return simplejson.load(data)


def comparevalue(entity, val):
    for i in entity[EDU_LABEL]:
        try:
            pref = i['prefLabel']
        except (KeyError, TypeError):
            continue
        if pref == val:
            return True
    return False


def select_entities(doc, pref_value):
    for entity in doc:
        try:
            select_entities(entity['children'], pref_value)
        except KeyError:
            pass
        if comparevalue(entity, pref_value):
            entities.append(entity)

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
                    csv_output(Country,
                               State,
                               Standard_Package,
                               Discipline,
                               grade_name(),
                               get_asn_id(grandchild['id']),
                               get_asn_id(child['id']),
                               'TRUE')#,
                               #grandchild['asn_statementNotation'],
                               #grandchild['text'])


def general_id():
    return 'Grade'+gradefilter


def csv_output(*args):
    filename = general_id() + '_' + discpline.upper() + '.'+'csv'
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_ALL)
        writer.writerow(args)

    csvfile.close()

if __name__ == '__main__':
    NUM2NAME = {'1': 'FIRST',
                '2': 'SECOND',
                '3': 'THIRD',
                '6': 'SIXTH',
                'K': 'KINDERGARTEN'}
    gradefilter = NUM2NAME.get(sys.argv[1], '6')

    doc = get_doc(ELAURL)
    select_entities(doc, sys.argv[1])
    print len(entities)

    #    if discpline.lower() =="ela":
#        doc = get_doc(ELAURL)
#        e = select_entities(doc, gradefilter)
#        CCSS_ELA()
#    elif discpline.lower() == "math":
#        doc = get_doc(MATHURL)
#        e = select_entities(doc, gradefilter)
#        CCSS_Math()
#===============================================================================
# #check that all group levels are coming in