import sys
import urllib2
import simplejson
import argparse
##############
MATHURL ="https://s3.amazonaws.com/asnstaticd2l/data/manifest/D10003FB.json" #math
ELAURL="https://s3.amazonaws.com/asnstaticd2l/data/manifest/D10003FC.json"#ELA

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--discpline", help="Choose your discpline (Ela or Math)")
parser.add_argument("-g", "--grade", help="Choose your grade level")
args = parser.parse_args()
#discpline = args.discpline 
discpline = "ela"
#gradefilter = args.grade
gradefilter = "6"

#print vars
Country='USA'
State=''
Standard_Package='CCSS'
Discipline = discpline
Grade_Level = 'SIXES'

Parent_Id =''
Selectable = ''
Name = ''
Description =''

def get_doc(URL):
    req = urllib2.Request(URL)
    opener = urllib2.build_opener()
    data = opener.open(req)
    return simplejson.load(data)

EDU_LABEL = 'dcterms_educationLevel'
PREF_LABEL = 'prefLabel'

def comparevalue(entity,val):
        for i in entity[EDU_LABEL]:
            try:
                pref = i.get(PREF_LABEL)
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



def CCSS_Math_parent_notation():
    
    for elem in e:
        print elem['children']['asn_statementNotation']
          

            
def CCSS_ELA():
      print 'Country', ';',   'State', ';',   'Standard Package',  ';',  'Discipline', ';',   'Grade Level', ';',   'Ped Id',  ';',  'Parent Id',   ';', 'Selectable',   ';', 'Name',   ';', 'Description'
      for elem in e:
        #print header
        #if comparevalue(elem,gradefilter):
        if elem['dcterms_description']['literal']:    
            print Country,';', State,';', Standard_Package,';', Discipline,';', Grade_Level,';', general_id(), ';', elem['dcterms_description']['literal'], ';','FALSE',';', elem['text'],';'," "
        else:
            print Country,';', State,';', Standard_Package,';', Discipline,';', Grade_Level,';', general_id(), ';', " ", ';','FALSE',';', elem['text'],';'," "
        for child in elem['children']:
            #if comparevalue(child,gradefilter):
                print Country,';', State,';', Standard_Package,';', Discipline,';', Grade_Level,';', " ",';', "   ", ';','FALSE',';', child['text'],';',' '
                for grandchild in child['children']:
                    #if comparevalue(grandchild,gradefilter):
                    print Country,';', State,';', Standard_Package,';', Discipline,';', Grade_Level,';',grandchild['asn_statementNotation'].strip(), ';', " ", ';','TRUE',';', Name,';',grandchild['text']
                   
def general_id():
    
    print 'Grade'+gradefilter

def grade_name():
    
    if gradefilter =='1':
        print 'FIRST'
    elif gradefilter =='2':
        print 'SECOND'
    elif gradefilter =='3':
        print 'THIRD'
    elif gradefilter =='4':
        print 'FOURTH'
    elif gradefilter =='5':
        print 'FIFTH'
    elif gradefilter =='6':
        print 'SIXTH'
    elif gradefilter =='7':
        print 'SEVENTH'
    elif gradefilter =='8':
        print 'EIGHTH'
    elif gradefilter =='9':
        print 'NINTH'
    elif gradefilter =='10':
        print 'TENTH'
    elif gradefilter =='11':
        print 'ELEVENTH'
    elif gradefilter =='12':
        print 'TWELFTH'
    else:
        print 'KINDERGARTEN'
    
if __name__ == '__main__':
    
    if discpline.lower() =="ela":
        doc = get_doc(ELAURL)
        e = select_entities(doc, gradefilter)
        CCSS_ELA()

    elif discpline.lower() == "math":
        doc = get_doc(MATHURL)
        e = select_entities(doc, gradefilter)
        #CCSS_Math()
        CCSS_Math_parent_notation()    