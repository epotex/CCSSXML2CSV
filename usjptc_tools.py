import sys
import urllib2
import simplejson
import argparse
import csv
import re
import time
import logging
import os

##############
"""Logging vars"""
logging.basicConfig(filename='t2k_jstc.log',level=logging.DEBUG, format='%(asctime)s %(message)s') 
logging.info('###############New Run###############')

"""Parser Vars"""
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--Discipline", help="Choose your Discipline (Ela or Math)")
parser.add_argument("-g", "--grade", help="Choose your grade level")
args = parser.parse_args()
#Discipline = args.Discipline """CMD Vars""" 
Discipline = "math"
#gradefilter = args.grade """CMD Vars"""
gradefilter = "9"
EDU_LABEL = 'dcterms_educationLevel'
PREF_LABEL = 'prefLabel'
"""Number to name dict"""
NUM2NAME = {'k': 'KINDERGARTEN',
            '1': 'FIRST',
            '2': 'SECOND',
            '3': 'THIRD',
            '4': 'FOURTH',
            '5': 'FIFTH',
            '6': 'SIXTH',
            '7': 'SEVENTH',
            '8': 'EIGHTH',
            '9': 'NINTH',
            '10': 'TENTH',
            '11': 'ELEVENTH',
            '12': 'TWELFTH'}#,
            #'6-8':'SIXTH-EIGHTH'}

"""Descipline to packege"""
Package = {'ela':'CCSS',
           'math':'CCSS',
           'txela':'TEKS',
           'txmath':'TEKS',
           'science':'NGSS'
           }

"""State by discipline"""
stats_list = {'ela':'',
              'math':'',
              'txela': 'TEXAS',
              'txmath': 'TEXAS',
              'science':'NGSS'
              }
"""Name of packege by descipline"""
names = {'ela':'Common Core State Standards',
         'math':'Common Core State Standards',
         'txela':  'Texas Essential Knowledge and Skills',
         'txmath': 'Texas Essential Knowledge and Skills',
         'science':'Next Generation Science Standards'
         }
"""Descipline by descipline arg"""
Discip = {'txela':'ELA',
          'txmath': 'MATH',
          'ela':'ELA',
          'math':'MATH',
          'science':'SICENCE'
          }
urls = {'math' :'MATHURL',
        'ela':'ELAURL',
        'txela':'TXELA',
        'txmath':'TXMATH',
        'science':'SICENCE'
        }
"""Json URLS list"""
urls = {'math' :'https://s3.amazonaws.com/asnstaticd2l/data/manifest/D10003FB.json',
        'ela':'https://s3.amazonaws.com/asnstaticd2l/data/manifest/D10003FC.json',
        'txela':'https://s3.amazonaws.com/asnstaticd2l/data/manifest/D100036C.json',
        'txmath':'https://s3.amazonaws.com/asnstaticd2l/data/manifest/D2486388.json',
        'science':'https://asn.jesandco.org/resources/D2454348_manifest.json'}
try:
    URL = urls[Discipline.lower()]
    URL = urls[Discipline.lower()]
    discipline_name = Discip[Discipline.lower()]
    name = names[Discipline.lower()]
    State =stats_list[Discipline.lower()]
    Standard_Package = Package[Discipline.lower()]
    grade_name = NUM2NAME[gradefilter]
except KeyError:
    pass
Country='USA'
def usage():
    print "Usage:"
    print "t2k_jstc.py -d Discipline -g Grade Level"
    print "Example:"
    print "t2k_jstc.py -d ela -g 7"
    print " "
    print "Currently the following standards supported:"
    print "Standards for ELA"
    print "##########"
    print "Texas standards| txela(for the -d option)"
    print "CCSS standards| ela(for the -d option)"
    print "##########"
    print " "
    print "Standards for Math"
    print "##########"
    print "Texas standards| txmath(for the -d option)"
    print "CCSS standards| math(for the -d option)"
    print "Standards for Science"
    print "##########"
    print "Science  standards| Science(for the -d option)"
  
#Functions:

"""Get the element grade level"""
def get_edu_label(element):
    for age in element[EDU_LABEL]:
        try:
            return age.get(PREF_LABEL)[0]
        except (TypeError, AttributeError):
            continue
"""Set the general ID + output file name prefix"""
def general_id():
    return 'Grade'+'_'+gradefilter

"""Set file name"""
filename = general_id() + '_' + Discipline.upper() + '.'+'csv'

"""Get json """
def get_doc(URL):
    req = urllib2.Request(URL)
    opener = urllib2.build_opener()
    data = opener.open(req)
    logging.info('Read complete')
    return simplejson.load(data)

"""Csv writer """
def csv_output(*args):

    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', lineterminator='\n', quoting=csv.QUOTE_ALL)
        writer.writerow(args)
    csvfile.close()

"""Get entity by grade level """    
def comparevalue(entity, val):
    for i in entity[EDU_LABEL]:
        try:
            pref = i[PREF_LABEL]
        except (KeyError, TypeError):
            continue
        if pref == val:
            return True
    return False

"""Create entities list"""            
def select_entities(doc, pref_value):
    entities = []
    for entity in doc:
        if comparevalue(entity, pref_value):
            entities.append(entity)
    return entities

"""Get the ASN identifier """
def get_asn_id(urlid):
    if urlid:
        asnid = re.findall("([^\/]+)$", str(urlid))
        return asnid[0]


"""Create the "StatementNotation" for TEKS standards"""

def tx_notation(child,father):
    noteid = re.findall("s/\([^)]*\)//", father['asn_listID'].strip())
    cnoteid = re.findall("s/\([^)]*\)//", child['asn_listID'].strip())
    for note in father['asn_listID'].strip():
        for childnote in child['asn_listID'].strip():
            return noteid[0], cnoteid[0] 
        
def general_notetion(item):
    try:
        return  item['asn_statementNotation'].strip()
    except KeyError:
        pass   
    