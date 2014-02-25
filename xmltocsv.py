#!/usr/bin/python
import csv
import urllib2
import time
import logging
import sys
import os
import argparse
from xml.dom.minidom import parseString
#Global Vars:
logging.basicConfig(filename='logxml2csv.log',level=logging.DEBUG, format='%(asctime)s %(message)s') 
mathfile = "Math.xml"
elafile = "ela-literacy.xml"


#seperator for the log file
logging.info('###############New Run###############')


#Usage

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--discpline", help="Choose your discpline (Ela or Math)")
parser.add_argument("-g", "--grade", help="Choose your grade level")
args = parser.parse_args()
discpline = args.discpline 
gradelevel = args.grade
logging.info('Discpline is: args.discpline')
logging.info('Grade level is: args.grade')


#Functions:

def download(xmlurl): #Downloading the right ccss file according selection
	xmlin = urllib2.urlopen(xmlurl)
	logging.info('Downloading the latest Math CCSS')
	xmloutput = open('xmli-in.xml','wb')
	xmloutput.write(xmlin.read())
	xmloutput.close()
	logging.info('Download complete')

def parser(discpline, xml_file):
	logging.info('Starting parser...')
        file = open(xml_file,'r')
        data = file.read()
        file.close()
        dom = parseString(data)
        xmlTag = dom.getElementsByTagName(user_string)[0].toxml()

        xmlData = xmlTag.replace('<tagName>','').replace('</tagName>','')
        print xmlTag
        print xmlData
		

#script:

#remove old files
logging.info('Removing any old CCSS files')
os.system("rm -rf ela-literacy.xml*")
os.system("rm -rf Math.xml*")

#checking for discipline 3 = ELA else - math
if args.discpline.lower() == "ela":
	logging.info('Downloading the latest ELA CCSS file')
	os.system("wget http://www.corestandards.org/ela-literacy.xml")
#	download(elaurl);
	parser(gradelevel,elafile)

else:
        logging.info('Downloading the latest Math CCSS file')
        os.system("wget http://www.corestandards.org/Math.xml")
#       download(mathurl);
	parser(u_string,mathfile)

 
