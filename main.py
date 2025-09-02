import time
from app import App

if __name__ == "__main__":
    print("Starting App...")
    app = App()

    while True:
        try:
            app.updateUsersData()
            app.checkUsageAndNotify()
        except Exception as error:
            print(error)

        time.sleep(3600)