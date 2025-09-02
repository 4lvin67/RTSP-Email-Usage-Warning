import requests

class SMS:
    def __init__(self, apiUrl, apiKey):
        self.apiUrl = apiUrl
        self.apiKey = apiKey
    
    def sendSMS(self, number, message):
        print("Sending SMS...")
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

        print("sendSMS() - ", response.text)
