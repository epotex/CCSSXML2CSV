import urllib2
xmlin = urllib2.Request("http://www.corestandards.org/Math.xml", headers={'User-Agent: Mozilla/5.0' : "Chrome"})
#xmlin = urllib2.urlopen("http://www.corestandards.org/Math.xml")
xmloutput = open('xmli-in.xml','wb')
xmloutput.write(xmlin.read())
xmloutput.close()
