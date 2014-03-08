import urllib2
import simplejson


mathurl ="http://s3.amazonaws.com/asnstaticd2l/data/manifest/D10003FB.json"
#Global Vars:


#Lists:



if __name__ == '__main__':

    req = urllib2.Request(mathurl)
    opener = urllib2.build_opener()
    data = opener.open(req)
    json = simplejson.load(data)
   # ID = item.get('id')
    #asn_identifier = item.get('asn_identifier')
    for item in json:
        ID = item.get('id')
        Subject = item.get('dcterms_subject').get('prefLabel')
        Grades = item.get('dcterms_educationLevel')
        Description = item.get('dcterms_description').get('literal')
        Children = item.get('children')
        #print Children.get('dcterms_description')
        
        #if  item.get('dcterms_educationalLevel') is not None:
       # print item.get('dcterms_educationLevel')
        
def get_entity_grades_list(x):    
    for item in x:
        grade_levels = []
        for grade in Grades:
           grade_levels.append(grade['prefLabel'])
    print grade_levels
print    Children  
#   
for child in  Children:
     for entity in child:
         if  entity == 'asn_statementLabel':
             print entity
