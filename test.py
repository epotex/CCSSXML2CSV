#!/usr/bin/python
#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
#all these imports are standard on most modern python implementations
 
#open the xml file for reading:
file = open('xmlin.xml','r')
#convert to string:
data = file.read()
#close file because we dont need it anymore:
file.close()
#parse the xml you got from the file
dom = parseString(data)
#retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
xmlTag = dom.getElementsByTagName('tagName')[0].toxml()
#strip off the tag (<tag>data</tag>  --->   data):
xmlData=xmlTag.replace('<tagName>','').replace('</tagName>','')
#print out the xml tag and data in this format: <tag>data</tag>
print xmlTag
#just print the data
print xmlData
