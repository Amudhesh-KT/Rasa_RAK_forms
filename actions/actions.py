# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Text, List, Any, Dict
from rasa_sdk.events import SlotSet
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []
#****************************************RAISE_COMPLAINT****************************************************
class ValidateComplaintForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_raise_complaint_form"

    def validate_r_username(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your user name is {slot_value}.")
        return {"r_username": slot_value}
    
    def validate_r_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your email is {slot_value}.")
        return {"r_email": slot_value}
    

    def validate_r_location(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your location is {slot_value}.")
        return {"r_location": slot_value}

    def validate_r_complaint_details(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your complaint details is {slot_value}.")
        return {"r_complaint_details": slot_value}
    
    def validate_r_attachments(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your attachments is {slot_value}.")
        return {"r_attachments": slot_value}
    

class ActionClearComplaintSlots(Action):
    def name(self) -> Text:
        return "action_clear_complaint_slots"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slots_to_clear = ["r_username", "r_email", "r_location", "r_complaint_details", "r_attachments"]
        slot_values = {slot: None for slot in slots_to_clear}
        return [SlotSet(slot, value) for slot, value in slot_values.items()]
    

#****************************************RAISE_COMPLAINT****************************************************    

#****************************************TRACK COMPLAINT******************************************************   
class ValidateTrackComplaintForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_track_complaint_form"
    
    def validate_t_complaint_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your complaint number is {slot_value}.")
        return {"t_complaint_number": slot_value}
    
    def validate_t_comments(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your comment is {slot_value}.")
        return {"t_comments": slot_value}
    
class ActionClearTrackSlots(Action):
    def name(self) -> Text:
        return "action_clear_track_slots"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slots_to_clear = ["t_complaint_number", "t_comments"]
        slot_values = {slot: None for slot in slots_to_clear}
        return [SlotSet(slot, value) for slot, value in slot_values.items()]
#****************************************TRACK COMPLAINT******************************************************

#****************************************SUGGESTIONS**********************************************************
class ValidateSuggestionForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_suggesstion_form"

    def validate_r_username(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your user name is {slot_value}.")
        return {"r_username": slot_value}
    
    def validate_r_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your email is {slot_value}.")
        return {"r_email": slot_value}
    

    def validate_r_location(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your location is {slot_value}.")
        return {"r_location": slot_value}

    def validate_s_suggestions(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your complaint details is {slot_value}.")
        return {"s_suggestions": slot_value}
    
    def validate_s_attachments(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    

 
        dispatcher.utter_message(text=f"Your attachments is {slot_value}.")
        return {"s_attachments": slot_value}
    
class ActionClearSuggestionSlots(Action):
    def name(self) -> Text:
        return "action_clear_suggestions_slots"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slots_to_clear = ["r_username", "r_email", "r_location", "s_suggestions", "s_attachments"]
        slot_values = {slot: None for slot in slots_to_clear}
        return [SlotSet(slot, value) for slot, value in slot_values.items()]
#****************************************SUGGESTIONS**********************************************************

