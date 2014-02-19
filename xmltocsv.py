#!/usr/bin/python
import csv
import urllib2
import time
import logging
import sys
import os

from xml.dom.minidom import parseString

#Global Vars:
logging.basicConfig(filename='xml2csv.log',level=logging.DEBUG, format='%(asctime)s %(message)s') 
mathurl = "http://162.159.240.19/Math.xml"
elaurl = "http://162.159.240.19/ela-literacy.xml"
grade = sys.argv[2] 


#Functions:
def download(xurl): #Downloading the right ccss file according selection
	xmlin = urllib2.urlopen(xurl)
	logging.info('Downloading the latest Math CCSS')
	xmloutput = open('xmlin.xml','wb')
	xmloutput.write(xmlin.read())
	xmloutput.close()
	logging.info('Download complete')


#Script:
#remove old files
logging.info('Removing any old CCSS files')

os.system("rm -rf ela-literacy.xml*")
os.system("rm -rf Math.xml*")

#checking for discipline 3 = ELA else - math
if len(sys.argv[1]) == 3:
	logging.info('Downloading the latest ELA CCSS file')
	os.system("wget http://www.corestandards.org/ela-literacy.xml")
#	download(elaurl);
        logging.info('Starting parser...')
	file = open('ela-literacy.xml','r')
	data = file.read()
	file.close()
	dom = parseString(data)
	xmlTag = dom.getElementsByTagName('GradeLevel')[0].toxml()
	xmlData=xmlTag.replace('<tagName>','').replace('</tagName>','')
	print xmlTag
	print xmlData


else:
        logging.info('Downloading the latest Math CCSS file')
        os.system("wget http://www.corestandards.org/Math.xml")
#       download(mathurl);
        logging.info('Starting parser...')
        file = open('Math.xml','r')
        data = file.read()
        file.close()
        dom = parseString(data)
        xmlTag = dom.getElementsByTagName('GradeLevel')[0].toxml()
        xmlData=xmlTag.replace('<tagName>','').replace('</tagName>','')
        print xmlTag
        print xmlData


 
