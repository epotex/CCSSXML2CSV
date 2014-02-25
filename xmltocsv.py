#!/usr/bin/python
import csv
import urllib2
import time
import logging
import os
import argparse
from xml.dom.minidom import parseString
#Global Vars:
logging.basicConfig(filename='logxml2csv.log',level=logging.DEBUG, format='%(asctime)s %(message)s') 
downfile = "xml-in.xml"
elaurl = "http://www.corestandards.org/ela-literacy.xml"
mathurl = "http://www.corestandards.org/Math.xml"

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
	xmlin = urllib2.Request(xmlurl, headers={'User-Agent: Mozilla/5.0' : "Chrome"})
	down = urllib2.urlopen (xmlin) 
	xmloutput = open('xml-in.xml','wb')
	xmloutput.write(down.read())
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
if os.path.isfile(downfile):
        os.remove(downfile)
	logging.info('xml-in.xml DELETED')
else:
	logging.info('Could not found any old file to remove...')

#checking for discipline 3 = ELA else - math
if args.discpline.lower() == "ela":
        logging.info('Downloading the latest Ela CCSS')
	download(elaurl);
	parser(gradelevel,downfile)

elif args.discpline.lower() == "math":
        logging.info('Downloading the latest Math CCSS')
        download(mathurl);
	parser(u_string,downfile)

else:
        logging.error('Unsupported discpline:, args.discpline')
	print "Please choose Ela or Math as a discpline"
	print "Couldn't set discpline"
	exit()
