# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import json
import numpy as np
from sklearn.neighbors import NearestNeighbors


def find_best_ans(user_preferences, data):
    user_vector = np.array([user_preferences[pref] for pref in user_preferences]).reshape(1, -1)
    vectors = []
    names = []

    for ans, attributes in data.items():
        ans_vector = np.array([attributes[pref] for pref in user_preferences])
        vectors.append(ans_vector)
        names.append(ans)

    vectors = np.array(vectors)

    nn = NearestNeighbors(n_neighbors=1, algorithm='brute', metric='euclidean')
    nn.fit(vectors)

    _, indices = nn.kneighbors(user_vector)
    best_ans_index = indices[0][0]
    best_ans = names[best_ans_index]

    return best_ans
import os
import json

def best_answer(cities_file_path):
    try:
        # Get the full path of the user.json file
        user_json_path = os.path.abspath('../data/user.json')
        print("Attempting to open:", user_json_path)
        
        # Check if the user.json file exists
        if not os.path.exists(user_json_path):
            print(f"File not found: {user_json_path}")
            return None
        
        # Open and read the user.json file
        with open(user_json_path, 'r') as user_file:
            user_data = json.load(user_file)

        # Uncomment if you need to check for missing preferences
        # missing_preferences = [pref for pref, value in user_data['preferences'].items() if value is None]
        # if missing_preferences:
        #     return demande_user_input(missing_preferences)
        
        # Get the full path of the cities.json file
        cities_full_path = os.path.abspath(cities_file_path)
        print("Attempting to open:", cities_full_path)
        
        # Check if the cities.json file exists
        if not os.path.exists(cities_full_path):
            print(f"File not found: {cities_full_path}")
            return None
        
        # Open and read the cities.json file
        with open(cities_full_path, 'r') as cities_file:
            data = json.load(cities_file)
        
        # Find the best answer
        best_ans = find_best_ans(user_data['preferences'], data)
        return best_ans

    except FileNotFoundError as e:
        print(f"File not found error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage with absolute path
absolute_path_to_cities_json = "/mnt/d/ENSEM/2A/CherguiAI/Project/backend/data/cities.json"
ans = best_answer(absolute_path_to_cities_json)




from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher




class ActionAskCity(Action):

    def name(self) -> Text:
        return "action_ask_city"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ans = "You should visit "
        ans += best_answer("../data/cities.json")
        dispatcher.utter_message(text=ans)

        return []
