import requests


def emotion_detector(text_to_analyse):
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=myobj)

    return response.json()
