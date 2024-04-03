import requests

WATSON_API_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
    "content-type": "application/json",
}

def emotion_detector(text_to_analyze):
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    r = requests.post(WATSON_API_URL, headers=HEADERS, json=data)
    if(r.status_code == 400):
        return {
            "anger": None,
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }
    json = r.json()
    json = json["emotionPredictions"][0]['emotion']
    json["dominant_emotion"] = max(json, key=json.get)
    return json