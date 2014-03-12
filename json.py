#!/usr/bin/env python
import sys
import urllib2
import simplejson

URL ="https://s3.amazonaws.com/asnstaticd2l/data/manifest/D10003FB.json"
EDU_LABEL = 'dcterms_educationLevel'
PREF_LABEL = 'prefLabel'
gradefilter = '6'

def get_doc():
    req = urllib2.Request(URL)
    opener = urllib2.build_opener()
    data = opener.open(req)
    return simplejson.load(data)

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

if __name__ == '__main__':
    doc = get_doc()
    e = select_entities(doc, gradefilter)
    for elem in e:
       print elem['id'],elem['text']