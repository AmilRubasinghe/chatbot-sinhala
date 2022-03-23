# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from html import entities
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction
# from rasa_sdk.forms import 
from pymongo import MongoClient
from actions.sub.databaseQuery import getMohDetails
from actions.sub.ontalogy import ontalogyCall
from actions.sub.ontalogy import getOntologyDetails
import pymongo
import logging
from daily import dailyData
from daily import dailyNewCases
from daily import dailyTotalCases
from daily import dailyNoOfIndividuals
from daily import dailyTotalDeath
from daily import dailyTodayDeades
from daily import dailyRecovered
from daily import dailyTotalpcrTest
from daily import dailylocalActiveCase

from daily import dailyglobalActiveCase
from daily import dailyglobalNewCase
from daily import dailyGlobalDeathsCase
from daily import dailyGlobalNewDeathCase
from daily import dailyGlobalRecoveryCase
from bson.json_util import dumps, loads
import json
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
)
import uuid
import random
import string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class ActionPositiveCase(Action):

    def name(self) -> Text:
        return "action_today_positive_case"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyNewCases() 
        dispatcher.utter_message(template="utter_todaypositivecase",localnewcases=message)
        return [] 
class ActionTotalPositive(Action):

    def name(self) -> Text:
        return "action_total_positive_case"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyTotalCases() 
        dispatcher.utter_message(template="utter_totalpositivecase",localtotalcases=message)
        return [] 
class ActionTotalDeath(Action):

    def name(self) -> Text:
        return "action_total_death"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyTotalDeath() 
        dispatcher.utter_message(template="utter_totaldeath",localdeaths=message)
        return [] 
class ActionHospitalIndividual(Action):

    def name(self) -> Text:
        return "action_individuals_in_hospital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyNoOfIndividuals() 
        dispatcher.utter_message(template="utter_individualsinhospital",localtotalnumberofindividualsinhospitals=message)
        return [] 
class ActionTodayDeath(Action):

    def name(self) -> Text:
        return "action_daily_Today_Deades"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyTodayDeades() 
        dispatcher.utter_message(template="utter_todaydeath",count=message)
        return [] 



class ActionLocalRecovary(Action):

    def name(self) -> Text:
        return "action_local_recovered"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyRecovered() 
        dispatcher.utter_message(template="utter_localrecovered",localrecovered=message[0])
        return [] 


class ActionPcrCount(Action):

    def name(self) -> Text:
        return "action_pcr_count"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyTotalpcrTest() 
        dispatcher.utter_message(template="utter_pcrcount",totalpcrtestingcount=message)
        return [] 
class ActionactiveCase(Action):

    def name(self) -> Text:
        return "action_active_case"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailylocalActiveCase() 
        dispatcher.utter_message(template="utter_activecase",localactivecases=message)
        return [] 


class ActionglobalactiveCase(Action):

    def name(self) -> Text:
        return "action_global_total_active_case"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyglobalActiveCase() 
        dispatcher.utter_message(template="utter_globalactivecase",globalactivecases=message)
        return [] 

class Actionglobalnewactivecase(Action):

    def name(self) -> Text:
        return "action_global_new_active_case"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyglobalNewCase() 
        dispatcher.utter_message(template="utter_globalnewcase",globalnewcases=message)
        return [] 
class Actionglobaltolatdeath(Action):

    def name(self) -> Text:
        return "action_global_total_death"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyGlobalDeathsCase() 
        dispatcher.utter_message(template="utter_globaltotaldeath",globaldeths=message)
        return [] 

class Actionglobalnewdeathcase(Action):

    def name(self) -> Text:
        return "action_global_new_death"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyGlobalNewDeathCase() 
        dispatcher.utter_message(template="utter_globalnewdeaths",globalnewdeath=message)
        return [] 

class Actionglobalrecovary(Action):

    def name(self) -> Text:
        return "action_global_recovary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyGlobalRecoveryCase() 
        dispatcher.utter_message(template="utter_globalrecovary",globalrecovery=message)
        return [] 

class dbTracker:
    def getDbConnection():
        
        # client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.auccv.mongodb.net/covid?retryWrites=true&w=majority")
        client = pymongo.MongoClient('localhost', 27017)
        db = client.covid
        logging.info("connection with database...")
        return db
    
class ActionMongoData(Action):

    def name(self) -> Text:
        return "action_database_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # client = pymongo.MongoClient('localhost', 27017)
        # db = client.covid
        print('call db')
        cityName = tracker.get_slot("city")
        print(cityName)    
        dbConecter  = dbTracker.getDbConnection()
        query = {"city":cityName}
        data = getMohDetails(query, dbConecter)
        list_cur = list(data)
        json_data = dumps(list_cur)
        objArray = json.loads(json_data)
        item =objArray[0]
        print(item)
        dispatcher.utter_message(template="utter_mohdetailsall",cityName=item['city'], mohtpNumber1=item['phoneNo'],mohaddress1 = item['address'])
        return [] 

def resetSymtoms():
    return [
                
                SlotSet("sore_throat", None),
                SlotSet("fever" , None),
                SlotSet("cough",None),
                SlotSet("headache",None),
                SlotSet("loss_taste",None),
                SlotSet("aches_pains",None),
                SlotSet("diarrhea",None),
                SlotSet("shortness_breath",None),
                SlotSet("confusion",None),
                SlotSet("chest_pain",None),
                SlotSet("bluish_lips",None),
                SlotSet("trouble_staying",None),
            ]

class ActionProcessSymptomList(Action):

     def name(self) -> Text:
         return "action_symptom_list"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = ""
        entities = tracker.latest_message['entities'].replace(" ", "_")
        print(entities)
        return
        if entities[0]['entity']  == 'sore_throat':
            SlotSet("sore_throat",entities[0]['value'])
            # if tracker.get_slot("sore_throat") == "None":
            #     print("true")
            #     SlotSet("sore_throat",entities[0]['value'])
            # else:
            #     print("false")
            #     return [SlotSet("sore_throat",None)]

        elif entities[0]['entity']  == 'fever':
            SlotSet("fever",entities[0]['value'])
            # if tracker.get_slot("fever") == None:
            #     SlotSet("fever",entities[0]['value'])
            # else:
            #     return [SlotSet("fever",None)]

        elif entities[0]['entity']  == 'cough':
            SlotSet("cough",entities[0]['value'])
            # if tracker.get_slot("cough") == None:
            #     SlotSet("cough",entities[0]['value'])
            # else:
            #     return [SlotSet("cough",None)]

        elif entities[0]['entity']  == 'headache':
            SlotSet("headache",entities[0]['value'])
            # if tracker.get_slot("headache") == None:
            #     SlotSet("headache",entities[0]['value'])
            # else:
            #     return [SlotSet("headache",None)]

        elif entities[0]['entity']  == 'loss_taste':
            SlotSet("loss_taste",entities[0]['value'])
            # if tracker.get_slot("loss_taste") == None:
            #     SlotSet("loss_taste",entities[0]['value'])
            # else:
            #     return [SlotSet("loss_taste",None)]

        elif entities[0]['entity']  == 'aches_pains':
            SlotSet("aches_pains",entities[0]['value'])
            # if tracker.get_slot("aches_pains") == None:
            #     SlotSet("aches_pains",entities[0]['value'])
            # else:
            #     return [SlotSet("aches_pains",None)]

        elif entities[0]['entity']  == 'diarrhea':
            SlotSet("diarrhea",entities[0]['value'])
            # if tracker.get_slot("diarrhea") == None:
            #     SlotSet("diarrhea",entities[0]['value'])
            # else:
            #     return [SlotSet("diarrhea",None)]

        elif entities[0]['entity']  == 'shortness_breath':
            SlotSet("shortness_breath",entities[0]['value'])
            # if tracker.get_slot("shortness_breath") == None:
            #     SlotSet("shortness_breath",entities[0]['value'])
            # else:
            #     return [SlotSet("shortness_breath",None)]

        elif entities[0]['entity']  == 'confusion':
            SlotSet("confusion",entities[0]['value'])
            # if tracker.get_slot("confusion") == None:
            #     SlotSet("confusion",entities[0]['value'])
            # else:
            #     return [SlotSet("confusion",None)]

        elif entities[0]['entity']  == 'chest_pain':
            SlotSet("chest_pain",entities[0]['value'])
            # if tracker.get_slot("chest_pain") == None:
            #     SlotSet("chest_pain",entities[0]['value'])
            # else:
            #     return [SlotSet("chest_pain",None)]

        elif entities[0]['entity']  == 'bluish_lips':
            SlotSet("bluish_lips",entities[0]['value'])
            # if tracker.get_slot("bluish_lips") == None:
            #     SlotSet("bluish_lips",entities[0]['value'])
            # else:
            #     return [SlotSet("bluish_lips",None)]

        elif entities[0]['entity']  == 'trouble_staying':
            SlotSet("trouble_staying",entities[0]['value'])
            # if tracker.get_slot("trouble_staying") == None:
            #     SlotSet("trouble_staying",entities[0]['value'])
            # else:
            #     return [SlotSet("trouble_staying",None)]

        elif entities[0]['entity']  == 'none':
            return [
                SlotSet("sore_throat", None),
                SlotSet("fever" , None),
                SlotSet("cough",None),
                SlotSet("headache",None),
                SlotSet("loss_taste",None),
                SlotSet("aches_pains",None),
                SlotSet("diarrhea",None),
                SlotSet("shortness_breath",None),
                SlotSet("confusion",None),
                SlotSet("chest_pain",None),
                SlotSet("bluish_lips",None),
                SlotSet("trouble_staying",None),
                ]
        return []

class ActionCorrectSymtomsList(Action):

     def name(self) -> Text:
         return "action_correct_symtoms"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        value = ["sore_throat","fever","cough","headache","loss_taste","aches_pains","diarrhea","shortness_breath","confusion","chest_pain","bluish_lips","trouble_staying"]
        for e in value:
            if not tracker.get_slot(e) == None:
                message = "{} - ✅".format(tracker.get_slot(e))
                dispatcher.utter_message(text= message)
       
        return []

class ActionClearSymptoms(Action):

     def name(self) -> Text:
         return "action_clear_symptom_list"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        
        return [
            SlotSet("sore_throat", None),
            SlotSet("fever" , None),
            SlotSet("cough",None),
            SlotSet("headache",None),
            SlotSet("loss_taste",None),
            SlotSet("aches_pains",None),
            SlotSet("diarrhea",None),
            SlotSet("shortness_breath",None),
            SlotSet("confusion",None),
            SlotSet("chest_pain",None),
            SlotSet("bluish_lips",None),
            SlotSet("trouble_staying",None),
        ]

class ActionontalogyData(Action):

    def name(self) -> Text:
        return "action_ontalogy_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        returnToSl = tracker.get_slot("return_to_srilanka")
        ratTest = tracker.get_slot("rat_test")
        closeContact = tracker.get_slot("close_contact")
        fullyVacinated = tracker.get_slot("fully_vacinated")
        highTransmitted = tracker.get_slot("high_transmitted")
        symtomsName = tracker.get_slot("symtoms")
        symptomsList=[]
        value = ["sore_throat","fever","cough","headache","loss_taste","aches_pains","diarrhea","shortness_breath","confusion","chest_pain","bluish_lips","trouble_staying"]
        for e in value:
            if not tracker.get_slot(e) == None:
                symptomsList.append(e)
        print(symptomsList)
       
        entityList = [ 
            {
              "entity" : "User",
              "value" : str(randomword(10))
            },
            {
              "entity" : "Symptom",
              "value" : symptomsList
            },
            {
              "entity" : "Test_Results",
              "value" : str(ratTest)
            },
            {
               "entity" : "Vacination",
               "value" : str(fullyVacinated)
            },
            {
              "entity" : "Contact_History",
              "value" : str(closeContact)
           },
           {
              "entity" : "Travel_History",
              "value" : str(highTransmitted)
           },
           {
              "entity" : "Immigration_History",
              "value" : str(returnToSl)
           }
        ]
   
       
        listString = json.dumps(entityList)

        dataList = ontalogyCall(json.loads(listString))
        print(dataList)
        dbConecter  = dbTracker.getDbConnection()
        query = {"case_id": str(dataList['case'])}
        dispatcher.utter_message(text='You are in '+dataList['case'])
        data = getOntologyDetails(query, dbConecter)
        print(data)
        list_cur = list(data)
        json_data = dumps(list_cur)
        objArray = json.loads(json_data)
        print(objArray)
        item =objArray[0]
        print(item)
        dispatcher.utter_message(text=item['recommendation_EN'])
        
        return[ SlotSet("sore_throat", None),
                SlotSet("fever" , None),
                SlotSet("cough",None),
                SlotSet("headache",None),
                SlotSet("loss_taste",None),
                SlotSet("aches_pains",None),
                SlotSet("diarrhea",None),
                SlotSet("shortness_breath",None),
                SlotSet("confusion",None),
                SlotSet("chest_pain",None),
                SlotSet("bluish_lips",None),
                SlotSet("trouble_staying",None),
                SlotSet("return_to_srilanka",None),
                SlotSet("rat_test",None),
                SlotSet("close_contact",None),
                SlotSet("high_transmitted",None),
                SlotSet("fully_vacinated",None),
                
                ]
