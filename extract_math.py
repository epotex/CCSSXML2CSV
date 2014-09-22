import tools


"""CCSS MATH Parsing"""
def CCSS_Math():
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
        for age in father[EDU_LABEL]:
            if age[PREF_LABEL] == gradefilter:
                csv_output(Country,
                           State,
                           Standard_Package,
                           discipline_name.upper().strip(),
                           grade_name,
                           general_notetion(father),
                           Standard_Package,
                           'FALSE',
                           father['text'].encode( "utf-8" )
                           )
                for children in father['children']:
                    csv_output(Country.strip(),
                        State.strip(),
                        Standard_Package.strip(),
                        discipline_name.upper().strip(),
                        grade_name,
                        general_notetion(children),
                        general_notetion(father),
                        'FALSE',
                        children['text'].encode( "utf-8" )                        
                        )
                    try:
                        for grandchild in children['children']:
                            csv_output(Country.strip(),
                                State.strip(),
                                Standard_Package.strip(),
                                discipline_name.upper().strip(),
                                grade_name,
                                general_notetion(grandchild),
                                general_notetion(children),
                                'FALSE',
                                general_notetion(grandchild),
                                grandchild['text'].encode( "utf-8" )                            
                                )
                    except KeyError:
                        try:
                            print children['children']
                        except KeyError:
                            continue
    logging.info('Json parding ended')