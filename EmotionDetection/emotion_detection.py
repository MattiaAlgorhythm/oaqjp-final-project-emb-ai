import requests
import json

def emotion_detector(text_to_analyze):
    # Check for blank input
    if not text_to_analyze.strip():
        # Return a dictionary with None values for blank entries
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=myobj, headers=header)
    
    # Parse the response JSON into a dictionary
    formatted_response = json.loads(response.text)
    
    # Correctly extract emotions and their scores from the nested structure
    emotions = formatted_response.get("emotionPredictions", [{}])[0].get("emotion", {})
    
    # Extract specific emotions
    anger_score = emotions.get("anger", 0)
    disgust_score = emotions.get("disgust", 0)
    fear_score = emotions.get("fear", 0)
    joy_score = emotions.get("joy", 0)
    sadness_score = emotions.get("sadness", 0)
    
    # Create a dictionary of the emotions
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Determine the dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return the final dictionary
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result
