# Project Name: Adana Guide

## Description
Adana Guide is a chatbot application designed to assist tourists by providing information and answering queries. The system leverages Rasa for natural language understanding and generation, Flask for server-side logic, and a React frontend for user interaction.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)

## Installation
To set up the project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/NIHIL3D/Tourism-Guide-Bot-AI-Powered-Interactive-Tourist-Assistant.git
    cd Tourism-Guide-Bot-AI-Powered-Interactive-Tourist-Assistant
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To run the application, you need to start both the Rasa server and the Flask server:

1. Train the Rasa model:
    ```sh
    rasa train
    ```

2. Start the Rasa action server:
    ```sh
    rasa run actions
    ```

3. Start the Rasa server:
    ```sh
    rasa run
    ```

4. Start the Flask server:
    ```sh
    python server.py
    ```

5. Start the React frontend:
    ```sh
    npm install
    npm start
    ```

Now, you can access the application by navigating to `http://localhost:3000` in your browser.

## Files
- `domain.yml`: Defines the intents, entities, slots, templates, and actions for the Rasa chatbot.
- `endpoints.yml`: Configuration file for the Rasa endpoints.
- `nlu.yml`: Contains the natural language understanding (NLU) training data.
- `stories.yml`: Specifies the training stories for Rasa, which are sequences of user inputs and bot responses.
- `actions.py`: Custom actions for the Rasa chatbot.
- `preferencesUpdate.py`: Script for updating user preferences.
- `requirements.txt`: Lists the Python dependencies for the project.
- `server.py`: Flask server to handle API requests.
- `App.js`: React component for the frontend.
