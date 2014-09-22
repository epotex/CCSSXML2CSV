import tools.py

"""CCSS ELA Parsing"""

def CCSS_ELA():
    logging.info('Json parding started')
    #First Line decleration
    csv_output(
           Country,
           State.strip(),
           Standard_Package.strip(),
           discipline_name.strip().upper(),
           grade_name.strip(),
           Standard_Package,
           None,
           'FALSE',
           name,
           None
           )   

    for father in e:
        csv_output('father',
                   Country,
                   State,
                   Standard_Package,
                   discipline_name.upper().strip(),
                   grade_name,
                   general_notetion(father),
                   Standard_Package,
                   'FALSE',
                   father['text'].encode( "utf-8" )
                   )
        for child in father['children']:
            for agegroup in child['dcterms_educationLevel']:
                if gradefilter in agegroup.values():
                    #Child
                    csv_output('child',
                        Country.strip(),
                        State.strip(),
                        Standard_Package.strip(),
                        discipline_name.upper().strip(),
                        grade_name,
                        general_notetion(child),
                        general_notetion(father),
                        'FALSE',
                        child['text'].encode( "utf-8" ),
                        )
                    for grandchild in child['children']:
                         try:
  
                             csv_output( 'grand',
                                Country,
                                State,
                                Standard_Package,
                                discipline_name.upper(),
                                grade_name,
                                #get_asn_id(grandchild['id']),
                                child['asn_statementNotation'].strip(),
                                #get_asn_id(children['id']),
                                grandchild['asn_statementNotation'].strip(),
                                'TRUE', 
                                grandchild['asn_statementNotation'].strip(),
                                grandchild['text'].encode( "utf-8" )
                                )
                       
                         except KeyError:
                             continue
                      
    logging.info('Json parding ended')