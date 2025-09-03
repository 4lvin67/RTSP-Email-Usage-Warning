class User:
    def __init__(self, email, number):
        self.email = email
        self.number = number
        self.userName = ''
        self.messageHistory = []
        self.maxMailboxSize = 0
        self.currentMailboxSize = 0
        self.mailboxUsage = 0
    
    def updateUserData(self, userName, maxMailboxSize, currentMailboxSize):
        self.userName = userName
        self.maxMailboxSize = maxMailboxSize / 1024 / 1024
        self.currentMailboxSize = round(currentMailboxSize / 1024 / 1024, 1)
        self.mailboxUsage = round(currentMailboxSize / maxMailboxSize * 100, 1)

    def __str__(self):
        string = f'userName: {self.userName}'
        string += f'\nemail: {self.email}'
        string += f'\nnumber: {self.number}'
        string += f'\nmaxMailboxSize: {self.maxMailboxSize} MB'
        string += f'\ncurrentMailboxSize: {self.currentMailboxSize} MB'
        string += f'\nmailboxUsage: {self.mailboxUsage}%'
        return string