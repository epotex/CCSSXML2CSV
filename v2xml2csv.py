#!/usr/bin/python
import csv
import urllib2
import time
import logging
import os
import argparse
from lxml import etree as ET

#Global Vars:
logging.basicConfig(filename='logxml2csv.log',level=logging.DEBUG, format='%(asctime)s %(message)s') 
downfile = "xml-in.xml"
elaurl = "http://s3.amazonaws.com/asnstatic/data/rdf/D10003FC.xml"
mathurl = "https://s3.amazonaws.com/asnstatic/data/rdf/D10003FB.xml"
TAG = 'LearningStandardItem'
field = '.*educationLevel'
gradelevel = 'http://purl.org/ASN/scheme/ASNEducationLevel/'
logging.info('###############New Run###############')
namespaces={'foaf': 'http://xmlns.com/foaf/0.1/', 'loc': 'http://www.loc.gov/loc.terms/relators/', 'gemq': 'http://purl.org/gem/qualifiers/', 'owl': 'http://www.w3.org/2002/07/owl#', 'cc': 'http://creativecommons.org/ns#', 'rdfs': 'http://www.w3.org/2000/01/rdf-schema#', 'dc': 'http://purl.org/dc/elements/1.1/', 'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#', 'dcterms': 'http://purl.org/dc/terms/', 'skos': 'http://www.w3.org/2004/02/skos/core#', 'asn': 'http://purl.org/ASN/schema/core/'}
#root = ET.fromstring(downfile)



#Functions:
#Downloading Function:
def download(xmlurl): #Downloading the right ccss file according selection
    xmlin = urllib2.Request(xmlurl, headers={'User-Agent: Mozilla/5.0' : "Chrome"})
    down = urllib2.urlopen (xmlin) 
    xmloutput = open('xml-in.xml','w')
    xmloutput.write(down.read())
    xmloutput.close()
    logging.info('Download complete')

def parser():
    
    tree = ET.parse(downfile).getroot()
    for element in tree.getchildren():
        #print element.xpath('*[local-name()=resorce]')
        print  element.xpath('*[local-name()="educationLevel"]') # '[/*[local-name()=resource]]')
                                                             
        #"//*[re:test
        
        #//*[@style] 
        #print element.xpath('/educationLevel/@*')
        #if element.xpath('*/%s[@resource=.*%s^]' % (field, gradelevel))
#<dcterms:educationLevel rdf:resource="http://purl.org/ASN/scheme/ASNEducationLevel/9"/>
        #print element.xpath('*')[3].attrib
        
        # % (field, gradelevel)):
        #for item in element:
         #    print item.xpath('*/*')# % (field, gradelevel)):
                 
        #print element.xpath([@'rdf:resource'='5']) 
            
#Script:
if __name__ == '__main__':

#Cleaning old filees
    logging.info('Removing any old CCSS files')
    if os.path.isfile(downfile):
        os.remove(downfile)
        logging.info('xml-in.xml DELETED')
    else:
        logging.info('Could not found any old file to remove...')
#checking for discipline ela or math, else -> exit
    
    logging.info('Downloading the latest Math CCSS')
    download(mathurl);
    parser()
    
