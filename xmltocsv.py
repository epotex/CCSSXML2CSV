#!/usr/bin/python
import csv
import urllib2
import time
import logging
import sys
import os
int = str(5)
from xml.dom.minidom import parseString

#Global Vars:
logging.basicConfig(filename='logxml2csv.log',level=logging.DEBUG, format='%(asctime)s %(message)s') 
mathfile = "Math.xml"
elafile = "ela-literacy.xml"
u_string = sys.argv[2] 
grade = sys.argv[3]
str(grade)

#Functions:
def download(xurl): #Downloading the right ccss file according selection
	xmlin = urllib2.urlopen(xurl)
	logging.info('Downloading the latest Math CCSS')
	xmloutput = open('xmlin.xml','wb')
	xmloutput.write(xmlin.read())
	xmloutput.close()
	logging.info('Download complete')

def parser(user_string,xml_file):
	logging.info('Starting parser...')
        file = open(xml_file,'r')
        data = file.read()
        file.close()
        dom = parseString(data)
#        xmlTag = dom.getElementsByTagName(user_string)[0].toxml()
	for s in dom.getElementsByTagName(user_string):
		if s.getAttribute(grade) == grade:
			print s.childNodes[0].data

#        xmlData = xmlTag.replace('<tagName>','').replace('</tagName>','')
#        print xmlTag
#        print xmlData

#script:
#remove old files
logging.info('Removing any old CCSS files')

os.system("rm -rf ela-literacy.xml*")
os.system("rm -rf Math.xml*")

#checking for discipline 3 = ELA else - math
if sys.argv[1].lower() == "ela":
	logging.info('Downloading the latest ELA CCSS file')
	os.system("wget http://www.corestandards.org/ela-literacy.xml")
#	download(elaurl);
	parser(u_string,elafile)

else:
        logging.info('Downloading the latest Math CCSS file')
        os.system("wget http://www.corestandards.org/Math.xml")
#       download(mathurl);
	parser(u_string,mathfile)

 
