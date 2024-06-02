import json
import numpy as np
from sklearn.neighbors import NearestNeighbors

user_scores = {}
pref = ""

def demande_user_input(missing_preferences):
    global pref
    pref = missing_preferences[0]
    return f"Enter your {pref} preference score (0-5): "

def get_user_input(input):
    global pref
    user_scores[pref] = int(input)

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

def update_user():
    global user_scores
    with open('data/user.json', 'r') as user_file:
        user_data = json.load(user_file)

    for pref, score in user_scores.items():
        user_data['preferences'][pref] = score
    user_scores = {}

    with open('data/user.json', 'w') as user_file:
        json.dump(user_data, user_file, indent=4)

def best_answer(d):
    with open('../../data/user.json', 'r') as user_file:
        user_data = json.load(user_file)

    # missing_preferences = [pref for pref, value in user_data['preferences'].items() if value is None]

    # if missing_preferences:
    #     return demande_user_input(missing_preferences)

    
    with open(d, 'r') as cities_file:
        data = json.load(cities_file)
    best_ans = find_best_ans(user_data['preferences'], data)
    return best_ans
