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
    for elem in e:
        #if comparevalue(elem,gradefilter):    
        print elem['id'],';',elem['text'],';', '#father#'
        for child in elem['children']:
            #if comparevalue(child,gradefilter):
                print child['id'],';',child['asn_statementNotation'],';','#child#',';',child['text']
                for grandchild in child['children']:
                    #if comparevalue(grandchild,gradefilter):
                        print grandchild['id'],';',grandchild['asn_statementNotation'],';','#grandchild#',';',grandchild['text']

def CCSS_ELA():
    for elem in e:
        #if comparevalue(elem,gradefilter):    
        print elem['id'],';',elem['text'],';', '#father#'
        for child in elem['children']:
            #if comparevalue(child,gradefilter):
                print child['id'],';',';','#child#',';',child['text']
                for grandchild in child['children']:
                    #if comparevalue(grandchild,gradefilter):
                        print grandchild['id'],';',grandchild['asn_statementNotation'],';','#grandchild#',';',grandchild['text']



    
if __name__ == '__main__':
    
    if args.discpline.lower() =="ela":
        doc = get_doc(ELAURL)
        e = select_entities(doc, gradefilter)
        CCSS_ELA()
    
    elif args.discpline.lower() == "math":
        doc = get_doc(MATHURL)
        e = select_entities(doc, gradefilter)
        CCSS_Math()
    