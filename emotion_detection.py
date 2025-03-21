import os
import requests
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

def emotion_detector(text_to_analyse):
    # Set up the authenticator
    #authenticator = IAMAuthenticator(os.getenv("API_IBM"))
    
    # Define the URL and headers
    url = os.getenv("URL_EMOTION_PREDICT")
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('API_IBM')}"  # Include the API key in the headers
    }
    
    # Prepare the input JSON
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    # Make the request
    response = requests.post(url, headers=headers, json=input_json)
    
    # Check the response
    if response.status_code == 200:
        return response.json()
    	# Return the label and score in a dictionary
	    #return {'label': label, 'score': score}
    elif response.status_code == 500:
        label = None
        score = None
    else:
        return f"Error: {response.status_code}, {response.text}"
    

emotion_detector("Hola estoy muy feliz")