import requests

class EmailServer:
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password

    def _getToken(self):
        url = self.server + 'api/v1/auth/authenticate-user'
        resp = requests.post(url, json={'username': self.username + "@rtsp.com.ph", 'password': self.password})
        accessToken = resp.json()['accessToken']
        return accessToken
    
    def getUsersData(self):
        url = self.server + '/api/v1/settings/domain/list-users-extra'
        accessToken = self._getToken()
        headers = {'Authorization': f'Bearer {accessToken}'}
        resp = requests.get(url, headers=headers)
        json = resp.json()
        return json['userData']
    
