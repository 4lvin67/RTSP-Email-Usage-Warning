import requests

class SMS:
    def __init__(self, apiUrl, apiKey):
        self.apiUrl = apiUrl
        self.apiKey = apiKey
    
    def sendSMS(self, number, message):
        payload = {
            "encoding": "AUTO",
            "track": None,
            "text": message,
            "source": "RTSP",
            "destination": number
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer " + self.apiKey
        }

        response = requests.post(self.apiUrl, json=payload, headers=headers)

        return response.text
