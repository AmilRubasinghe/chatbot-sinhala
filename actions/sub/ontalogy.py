import sys
import logging
from owlready2 import *
import json
import re
sys.path.append("C:/")
ONTOLOGY_PATH = "file://F:/fanal-year-project/covid-data-ontology.owl"

    

def ontalogyCall(dataList):
    print('call db')
    # Ontology initialization 
    onto = get_ontology(ONTOLOGY_PATH).load()
    print("ontology name = "+onto.name)
    print("working")
    symp=[]
    newList = dataList
    print(dataList)
    for e in newList:
            if(e["entity"] == "User"):
                name = e['value']

            if(e["entity"] == "Test_Results"):
                Test_Results = e['value']

            if(e["entity"] == "Symptom"):
                symptomList = (e['value'])
            
            if(e["entity"] == "Contact_History"):
                Contact_History = (e['value'])

            if(e["entity"] == "Travel_History"):
                Travel_History = (e['value'])
            
            if(e["entity"] == "Immigration_History"):
                Immigration_History = (e['value'])

    # Create user in ontology
    name = onto.Person(name)

    # Insert Symptoms Properties
    if(symptomList):
        name.hasSymptoms.append(True)
        for symptom in symptomList:
            symp = onto.Symptom(symptom)
            name.hasSymptom.append(symp)
    else:
        name.hasSymptoms.append(False)


    # Insert Data Properties
    if((Contact_History.lower() == 'yes') or (Travel_History.lower() == 'yes')):
        name.hadHistory.append(True)
    elif((Contact_History.lower() == 'no') or (Travel_History.lower() == 'no')):
        name.hadHistory.append(False)

    # Start Reasoner
    sync_reasoner(infer_property_values = True)
    print(name.__class__)
    l1 = list(name.is_a)
    print(l1)

    # extract case ID
    pattern1 = 'recommondation'
    pattern2 = 'case'
    recommendation = ""
    case = ""
    for i in l1:
        if(re.search(pattern1,str(i))):
                #print(str(i).replace(str(onto.name)+'.',""))
            recommendation = (str(i).replace(str(onto.name)+'.',""))
            
        if(re.search(pattern2,str(i))):
            case = (str(i).replace(str(onto.name)+'.',""))
        
    d = dict()
    d['recommendation'] = recommendation
    d['case'] = case
        
    print("d=",d)

    return d




def getOntologyDetails(dbQuery,dbConection):
    x = []
    ontalogyData = dbConection.Recommendation.find(dbQuery)
    for i in ontalogyData:
        x.append(i)
    logging.info("fetch the document from the data base")
    return x






# class ObjectRepository:
#     def foo(jsonstring):
#         lst = json.loads(jsonstring)
#         return lst

# class SinhalaOntologyRepository:
    
#     # Ontology initialization 
#     def SinhalaontologyInit(path):
        
#         onto = get_ontology(path).load()
#         print("ontology name = "+onto.name)
#         symp=[]
#         newList = ObjectRepository.foo(listString)
#         for e in newList:
#             if(e["entity"] == "User"):
#                 name = e['value']

#             if(e["entity"] == "Test_Results"):
#                 Test_Results = e['value']

#             if(e["entity"] == "Symptom"):
#                 symptomList = (e['value'])
            
#             if(e["entity"] == "Contact_History"):
#                 Contact_History = (e['value'])

#             if(e["entity"] == "Travel_History"):
#                 Travel_History = (e['value'])
            
#             if(e["entity"] == "Immigration_History"):
#                 Immigration_History = (e['value'])

#         # Create user in ontology
#         name = onto.Person(name)

#         # Insert Symptoms Properties
#         if(symptomList):
#             name.hasSymptoms.append(True)
#             for symptom in symptomList:
#                 symp = onto.Symptom(symptom)
#                 name.hasSymptom.append(symp)
#         else:
#             name.hasSymptoms.append(False)
        
#         #Insert Test Results Property
#         #if(Test_Results):
#             #testResults = onto.Test_result(Test_Results)
#             #name.covid_test_results.append(Test_Results)
        
#         # Insert Data Properties
#         if((Contact_History.lower() == 'yes') or (Travel_History.lower() == 'yes')):
#             name.hadHistory.append(True)
#         elif((Contact_History.lower() == 'no') or (Travel_History.lower() == 'no')):
#             name.hadHistory.append(False)
        
#         # Start Reasoner
#         sync_reasoner(infer_property_values = True)
#         print(name.__class__)
#         l1 = list(name.is_a)
#         print(l1)

#         # extract case ID
#         pattern1 = 'recommondation'
#         pattern2 = 'case'
#         recommendation = ""
#         case = ""
#         for i in l1:
#             if(re.search(pattern1,str(i))):
#                 #print(str(i).replace(str(onto.name)+'.',""))
#                 recommendation = (str(i).replace(str(onto.name)+'.',""))
            
#             if(re.search(pattern2,str(i))):
#                 case = (str(i).replace(str(onto.name)+'.',""))
        
#         d = dict()
#         d['recommendation'] = recommendation
#         d['case'] = case
        
#         print("d=",d)

#         return d