#!/usr/bin/env python

import csv
import urllib2
import simplejson

#Vars:
country='Country'
state='State'
standard_package ='CCSS'
discpline ='Math'
grade_level='FIFTH'
pedid='state notation'
parentid='to be add'
selectable=''
name=''

URL ="https://s3.amazonaws.com/asnstaticd2l/data/manifest/D10003FB.json"
EDU_LABEL = 'dcterms_educationLevel'
PREF_LABEL = 'prefLabel'

def csv_header():
    print Country, State, 'Standart Package', 'Discpline','Grade Level','Ped ID', 'Parent ID', 'Selectable', 'Name','Discription'

def csv_writer():
    with open(r"test.csv", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter =",",quoting=csv.QUOTE_MINIMAL)
        writer.writerow([country,state,standard_package,discpline,grade_level,pedid,parentid,selectable,name,discription])



def get_doc():
    req = urllib2.Request(URL)
    opener = urllib2.build_opener()
    data = opener.open(req)
    return simplejson.load(data)

def select_entities(doc, pref_value):
    entities = []
    for entity in doc:
        for i in entity[EDU_LABEL]:
            try:
                pref = i.get(PREF_LABEL)
            except AttributeError:
                continue
            if pref == pref_value:
                entities.append(entity)
                break
    return entities

def child():
    if child.get('asn_identifier'):
        id=child.get('asn_identifier').values()[0]
        pedid=child.get('asn_statementNotation')
        discription=child.get('text')
        print id,pedid,discription
                 
          
                  
        
if __name__ == '__main__':
    doc = get_doc()
    e = select_entities(doc, "5")
    for item in e:
        
        for child in  item['children']:
                 #print country,state,standard_package,discpline,grade_level,pedid,parentid,selectable,name,discription
                 for grandchild in child.get('children'):
                     print grandchild
        
           
                 #print child.get("text")#.get('asn_statementLabel')
                 #print country,state,standard_package,discpline,grade_level,pedid,parentid,selectable,name,discription    
                 #print id, pedid,discription 
         
