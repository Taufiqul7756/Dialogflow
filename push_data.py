import csv
import requests

# Set up your API endpoint and access token
api_endpoint = "https://dialogflow.googleapis.com/v2/projects/project_id/agent/sessions/kk:detectIntent"
access_token = ""

# Read the CSV file
with open("./data_6k_to_7k/6.8k_to_7k.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if presents
    # Loop through each row in the CSV file
    for row in reader:
        text = row[0]  # Assuming the text is in the first column

        # Create the request body
        request_body = {"queryInput": {"text": {"languageCode": "en", "text": text}}}

        # Set the request headers with the access token
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        # Make the API request with authentication
        response = requests.post(api_endpoint, json=request_body, headers=headers)

        # Check the status code to ensure the request was successful
        if response.status_code == 200:
            print(f"Successfully sent text: {text}")
        else:
            print(f"Error sending text: {text}")
