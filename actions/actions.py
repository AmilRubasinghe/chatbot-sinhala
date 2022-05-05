# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from html import entities
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction
# from rasa_sdk.forms import 
from pymongo import MongoClient
from actions.sub.databaseQuery import getMohDetails
from actions.sub.databaseQuery import getPhiDetails
from actions.sub.ontalogy import ontalogyCall
from actions.sub.ontalogy import getOntologyDetails
import pymongo
from bson.json_util import dumps, loads
import logging
import json
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

class dbTracker:
    def getDbConnection():
        # client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.auccv.mongodb.net/covid?retryWrites=true&w=majority")
        client = pymongo.MongoClient('localhost', 27017)
        db = client.covid
        logging.info("connection with database...")
        return db

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
        entities = tracker.latest_message['entities']
        if entities[0]['entity']  == 'sore_throat':
            SlotSet("sore_throat",entities[0]['value'])
        elif entities[0]['entity']  == 'fever':
            SlotSet("fever",entities[0]['value'])
        elif entities[0]['entity']  == 'cough':
            SlotSet("cough",entities[0]['value'])
        elif entities[0]['entity']  == 'headache':
            SlotSet("headache",entities[0]['value'])
        elif entities[0]['entity']  == 'loss_taste':
            SlotSet("loss_taste",entities[0]['value'])
        elif entities[0]['entity']  == 'aches_pains':
            SlotSet("aches_pains",entities[0]['value'])
        elif entities[0]['entity']  == 'diarrhea':
            SlotSet("diarrhea",entities[0]['value'])
        elif entities[0]['entity']  == 'shortness_breath':
            SlotSet("shortness_breath",entities[0]['value'])
        elif entities[0]['entity']  == 'confusion':
            SlotSet("confusion",entities[0]['value'])
        elif entities[0]['entity']  == 'chest_pain':
            SlotSet("chest_pain",entities[0]['value'])
        elif entities[0]['entity']  == 'bluish_lips':
            SlotSet("bluish_lips",entities[0]['value'])
        elif entities[0]['entity']  == 'trouble_staying':
            SlotSet("trouble_staying",entities[0]['value'])
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

class ActionCorrectSymtomsList(Action):
     def name(self) -> Text:
         return "action_correct_symtoms"
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        showingList = [ 
            {
              "entity" : "sore_throat",
              "value" : "උගුරෙ ආසාදනය"
            },
            {
              "entity" : "fever",
              "value" : "උණ"
            },
            {
              "entity" : "cough",
              "value" : "කැස්ස"
            },
            {
               "entity" : "headache",
               "value" : "හිසරදය"
            },
            {
              "entity" : "loss_taste",
              "value" : "සුවඳ හෝ රස දැනීම අඩුවීම"
           },
           {
              "entity" : "aches_pains",
              "value" : "හන්දිපත් රුදාව"
           },
           {
              "entity" : "diarrhea",
              "value" : "පාචනය"
           },
           {
              "entity" : "shortness_breath",
              "value" : "හුස්ම කෙටිවීම"
           },
           {
              "entity" : "confusion",
              "value" : "වියාකූල බව"
           },
           {
              "entity" : "chest_pain",
              "value" : "පපුවේ වේදනාව"
           },
           {
              "entity" : "bluish_lips",
              "value" : "තොල් දම් පැහැ වීම"
           },
           {
              "entity" : "trouble_staying",
              "value" : "නිදිමත ගතිය"
           },
        ]
        
        for e in showingList:
            if not tracker.get_slot(e["entity"]) == None:
                print(tracker.get_slot(e["entity"]))
                message = "{} - ✅".format(e["value"])
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
        # dispatcher.utter_message(text='You are in '+dataList['case'])
        data = getOntologyDetails(query, dbConecter)
        print(data)
        list_cur = list(data)
        json_data = dumps(list_cur)
        objArray = json.loads(json_data)
        print(objArray)
        item =objArray[0]
        print(item)
        dispatcher.utter_message(text=item['recommendation_SIN'])
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

class ActionPositiveCase(Action):

    def name(self) -> Text:
        return "action_today_positive_case"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyNewCases() 
        print(message)
        dispatcher.utter_message(template="utter_todaypositivecase",localnewcases=message["value"], time= message["time"])
        return [] 
class ActionTotalPositive(Action):

    def name(self) -> Text:
        return "action_total_positive_case"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyTotalCases() 
        print(message)
        dispatcher.utter_message(template="utter_totalpositivecase",localtotalcases=message["value"], time= message["time"])
        return [] 
class ActionTotalDeath(Action):

    def name(self) -> Text:
        return "action_total_death"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyTotalDeath() 
        print(message)
        dispatcher.utter_message(template="utter_totaldeath",localdeaths=message["value"], time= message["time"])
        return [] 
class ActionHospitalIndividual(Action):

    def name(self) -> Text:
        return "action_individuals_in_hospital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyNoOfIndividuals() 
        print(message)
        dispatcher.utter_message(template="utter_individualsinhospital",localtotalnumberofindividualsinhospitals=message["value"], time= message["time"])
        return [] 
class ActionTodayDeath(Action):

    def name(self) -> Text:
        return "action_daily_Today_Deades"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyTodayDeades() 
        print(message)
        dispatcher.utter_message(template="utter_todaydeath",count=message["value"], time= message["time"])
        return [] 



class ActionLocalRecovary(Action):

    def name(self) -> Text:
        return "action_local_recovered"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyRecovered() 
        print(message)
        dispatcher.utter_message(template="utter_localrecovered",localrecovered=message["value"], time= message["time"])
        return [] 


class ActionPcrCount(Action):

    def name(self) -> Text:
        return "action_pcr_count"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyTotalpcrTest() 
        print(message)
        dispatcher.utter_message(template="utter_pcrcount",totalpcrtestingcount=message["value"], time= message["time"])
        return [] 
class ActionactiveCase(Action):

    def name(self) -> Text:
        return "action_active_case"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailylocalActiveCase() 
        print(message)
        dispatcher.utter_message(template="utter_activecase",localactivecases=message["value"], time= message["time"])
        return [] 


class ActionglobalactiveCase(Action):

    def name(self) -> Text:
        return "action_global_total_active_case"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyglobalActiveCase() 
        print(message)
        dispatcher.utter_message(template="utter_globalactivecase",globalactivecases=message["value"], time= message["time"])
        return [] 

class Actionglobalnewactivecase(Action):

    def name(self) -> Text:
        return "action_global_new_active_case"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyglobalNewCase() 
        print(message)
        dispatcher.utter_message(template="utter_globalnewcase",globalnewcases=message["value"], time= message["time"])
        return [] 
class Actionglobaltolatdeath(Action):

    def name(self) -> Text:
        return "action_global_total_death"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyGlobalDeathsCase() 
        dispatcher.utter_message(template="utter_globaltotaldeath",globaldeths=message["value"], time= message["time"])
        return [] 

class Actionglobalnewdeathcase(Action):

    def name(self) -> Text:
        return "action_global_new_death"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyGlobalNewDeathCase() 
        dispatcher.utter_message(template="utter_globalnewdeaths",globalnewdeath=message["value"], time= message["time"])
        return [] 

class Actionglobalrecovary(Action):

    def name(self) -> Text:
        return "action_global_recovary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message  = dailyGlobalRecoveryCase() 
        dispatcher.utter_message(template="utter_globalrecovary",globalrecovery=message["value"], time= message["time"])
        return [] 


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
        query = {"sinDistrict":cityName}
        data = getMohDetails(query, dbConecter)
        list_cur = list(data)
        json_data = dumps(list_cur)
        objArray = json.loads(json_data)
        for item in objArray:
            print(item)
            dispatcher.utter_message(template="utter_mohdetailsall",cityName=item['sinDistrict'], mohtpNumber1=item['mobile'],mohaddress1 = item['sinAddress'])


        # item =objArray[0]
        return [] 

class ActionMongoData(Action):

    def name(self) -> Text:
        return "action_phiDatabase_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # client = pymongo.MongoClient('localhost', 27017)
        # db = client.covid
        print('call db')
        cityName = tracker.get_slot("city")
        print(cityName)    
        dbConecter  = dbTracker.getDbConnection()
        query = {"sinDistrict":cityName}
        data = getPhiDetails(query, dbConecter)
        list_cur = list(data)
        json_data = dumps(list_cur)
        objArray = json.loads(json_data)
        for item in objArray:
            print(item)
            dispatcher.utter_message(template="utter_phidetailsall",cityName=item['sinDistrict'],phiName=item['sinName'],phitpNumber=item['mobile'],phiEmail=item['email'],phiaddress = item['sinAddress'])

        # item =objArray[0]
        return [] 