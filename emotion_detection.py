import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def emotion_detector(text_to_analyse):
    # Define the URL and headers
    url = os.getenv("URL_EMOTION_PREDICT")
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # Prepare the input JSON
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    response = requests.post(url, headers=headers, json=input_json)
    print(response.text)
        
    # Check the response
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 500:
        label = None
        score = None
    else:
        return f"Error: {response.status_code}, {response.text}"