import requests


def send_message_to_dialogflow(message):
    dialogflow_api_url = "https://dialogflow.googleapis.com/v2/projects/palette-chat-qljh/agent/sessions/kk:detectIntent"
    headers = {
        "Authorization": "Bearer ya29.a0AfB_byDjqtjSs5b5FIertUQv4rw1QXf-X1wUSGTe5WjicB_ujG-PET9QVxbGb5fHpqVqKddLiNDx1ruvkl9k7j4ntXS_AKNT2ti8oYq8J-rL8pHWvsLTSWPGRuRzTq6giNH_SKmvtS05zrHMXtgRfTaQADosfSuaF-xk2hAaCgYKAQASARASFQHsvYlsuVFSfuFwWFeZqFQsQprbcA0174",
        "Content-Type": "application/json",
    }
    payload = {
        "queryInput": {
            "text": {"text": message, "languageCode": "en"}  # Send a single message
        }
    }

    response = requests.post(dialogflow_api_url, json=payload, headers=headers)
    return response.json()


def classify_intent(response):
    intent = response["queryResult"]["intent"]["displayName"]
    return intent


# List of messages you want to classify
messages_to_classify = [
    "Phone number pls",
    "Commercial Design Consultation",
    "Is anyone available to chat?",
    "what about pricing?",
    "\u0995\u09bf",
    "http://127.0.0.1:5500/index.html",
    "Phone pick korena kew",
    "Did you add my number?",
    "I called you. I haven't received a response yet",
    "My number is 01727102192",
]

# Initialize a dictionary to store messages by intent
message_groups = {}

# Classify and organize messages by intent
for message in messages_to_classify:
    dialogflow_response = send_message_to_dialogflow(message)
    detected_intent = classify_intent(dialogflow_response)

    if detected_intent == "Junk-Intent-Default":
        detected_intent = "Junk-intent"  # Merge into Junk-intent

    if detected_intent not in message_groups:
        message_groups[detected_intent] = []

    message_groups[detected_intent].append(message)

# Print the result in the desired format
for intent, messages in message_groups.items():
    messages_str = ", ".join([f'"{msg}"' for msg in messages])
    print(f"{intent} : {{ {messages_str} }}")
