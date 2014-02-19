#!/usr/bin/python
import csv
import urllib2
import time
import logging
import sys
import xmlutils 
from xml.dom.minidom import parseString

#Global Vars:

logging.basicConfig(filename='xml2csv.log',level=logging.DEBUG, format='%(asctime)s %(message)s') 
mathurl = "http://162.159.240.19/Math.xml"
elaurl = "http://162.159.240.19/ela-literacy.xml"

#Functions:
def download(xurl): #Downloading the right ccss file according selection
	xmlin = urllib2.urlopen(xurl)
	logging.info('Downloading the latest Math CCSS')
	xmloutput = open('xmlin.xml','wb')
	xmloutput.write(xmlin.read())
	xmloutput.close()
	logging.info('Download complete')


#Script:
#checking for discipline 3 = ELA else - math
if len(sys.argv[1]) == 3:
        logging.info('Downloading the latest ELA CCSS file')
	download(elaurl);

else:
        logging.info('Downloading the latest Math CCSS file')
        download(mathurl)



