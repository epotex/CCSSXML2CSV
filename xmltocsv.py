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
elaurl = "http://www.corestandards.org/ela-literacy.xml"
mathurl = "http://www.corestandards.org/Math.xml"
TAG = 'LearningStandardItem'
field = 'GradeLevel'
logging.info('###############New Run###############')

#Usage/parser

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--discpline", help="set the discpline (Ela or Math)")
parser.add_argument("-g", "--grade", help="set the grade level")
args = parser.parse_args()
discpline = args.discpline 
gradelevel = args.grade
logging.info('Discpline is: args.discpline')
logging.info('Grade level is: args.grade')
#Functions:
discpline = "math"
gradelevel = "5"
#Downloading Function:
def download(xmlurl): #Downloading the right ccss file according selection
	xmlin = urllib2.Request(xmlurl, headers={'User-Agent: Mozilla/5.0' : "Chrome"})
	down = urllib2.urlopen (xmlin) 
	xmloutput = open('xml-in.xml','wb')
	xmloutput.write(down.read())
	xmloutput.close()
	logging.info('Download complete')

#Parser Finction:
def main():
    elements = []
    tree = ET.parse(downfile).getroot()
    for element in tree.getchildren():
        if element.xpath('*/%s[.=%s]' % (field, gradelevel)):
            yield element
#	    return  element

#CSV Writer Function
def csv_writer():
	 with open(r"test.csv", "wb") as csv_file:
                writer = csv.writer(csv_file, delimiter =",",quoting=csv.QUOTE_MINIMAL)
		writer.writerow([a.xpath('*/StatementCode')[0].text, a.xpath('*/Statement')[0].text, a.xpath('*/description')[0].text, a.xpath('*/GradeLevel')[0].text])


#Script:
if __name__ == '__main__':

#Cleaning old filees
	logging.info('Removing any old CCSS files')
	if os.path.isfile(downfile):
        	os.remove(downfile)
		logging.info('xml-in.xml DELETED')
	else:
		logging.info('Could not found any old file to remove...')
#===============================================================================
# #checking for discipline ela or math, else -> exit
# 	if args.discpline.lower() == "ela":
# 		logging.info('Downloading the latest Ela CCSS')
# 		download(elaurl)
# 		for a in main():
# 			csv_writer()
# 	elif args.discpline.lower() == "math":
# 		logging.info('Downloading the latest Math CCSS')
# 		download(mathurl)
# 		for a in main():
# 			print a
#                        #  csv_writer()
# 	else:
#         	logging.error('Unsupported discpline:, args.discpline')
# 		print "Please choose Ela or Math as a discpline"
# 		print "Couldn't set discpline"
# 		exit()
#===============================================================================
download(mathurl)
for a in main():
	print a

