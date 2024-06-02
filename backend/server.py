from flask import Flask, request, jsonify
import json
import requests
from preferencesCalculation import best_answer, get_user_input, demande_user_input, update_user

app = Flask(__name__)
RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"
firstAns = False
missing_preferences = []

def load_user_data():
    with open('data/user.json', 'r') as user_file:
        return json.load(user_file)

def check_missing_preferences(user_data):
    return [pref for pref, value in user_data['preferences'].items() if value is None]

@app.route('/home', methods=['GET', 'POST'])
def check():
    global firstAns, missing_preferences
    user_data = load_user_data()
    missing_preferences = check_missing_preferences(user_data)

    if missing_preferences:
        return jsonify(demande_user_input(missing_preferences))
    # firstAns = True
    return jsonify("We are good to start how can I help you!")

@app.route('/Search', methods=['POST'])
def Search():
    global firstAns, missing_preferences
    message = request.json["prompt"]
    user_data = load_user_data()
    missing_preferences = check_missing_preferences(user_data)

    if missing_preferences:
        get_user_input(message)
        update_user()
        return check()
    if firstAns:
        firstAns = False
        return jsonify("We are good to start how can I help you!")
    
    # Use requests.post to send the message to RASA
    rasa_response = requests.post(RASA_API_URL, json={'message': message})
    rasa_response_json = rasa_response.json()
    print("rasa response: ", rasa_response_json)
    bot_response = rasa_response_json[0]['text'] if rasa_response_json else 'Sorry something went wrong goes wrong.'
    return jsonify(bot_response)

if __name__ == '__main__':
    app.run(debug=True)
