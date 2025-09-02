import os
from dotenv import load_dotenv
import json
from user import User
from email_server import EmailServer
from sms import SMS
from ai import Ai

class App:
    users: dict[str, User] = {}
    usageWarningThreshold = 90.0

    def __init__(self):
        load_dotenv()
        self.initUsers(os.environ.get("PEOPLE_INFO"))
        self.emailServer = EmailServer(
            os.getenv('SERVER_ADDRESS'),
            os.getenv('USERNAME'),
            os.getenv('PASSWORD')
        )
        self.sms = SMS(
            os.getenv('SMS_API_URL'),
            os.getenv('SMS_API_KEY')
        )
        self.ai = Ai(os.environ.get("GEMINI_API_KEY"))


    def initUsers(self, peopleInfoString):
        peopleInfo = json.loads(peopleInfoString)
        for person in peopleInfo:
            self.users[person['email']] = User(person['email'], person['number'])

    def updateUsersData(self):
        usersData = self.emailServer.getUsersData()
        for data in usersData:
            if data['emailAddress'] in self.users:
                self.users[data['emailAddress']].updateUserData(
                    data['userName'],
                    data['maxMailboxSize'],
                    data['currentMailboxSize']
                )

    def checkUsageAndNotify(self):
        for email in self.users:
            if self.users[email].mailboxUsage >= self.usageWarningThreshold:

                message = f"User: {self.users[email].userName}"
                message += f"\nMailbox Limit: {self.users[email].maxMailboxSize} MB"
                message += f"\nMailbox Size: {self.users[email].currentMailboxSize} MB"
                message += f"\nMailbox Usage: {self.users[email].mailboxUsage}%"

                self.users[email].messageHistory = self.ai.generateContents("user", message, self.users[email].messageHistory)

                aiMessage = self.ai.aiResponse(self.users[email].messageHistory)
                print("Ai Message:", aiMessage)

                self.sms.sendSMS(self.users[email].number, aiMessage)

                self.users[email].messageHistory = self.ai.generateContents("model", aiMessage, self.users[email].messageHistory)

            else:
                self.users[email].messageHistory = []