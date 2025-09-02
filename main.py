import time
from classes.app import App

USAGE_THRESHOLD = 90.0
TIME_INTERVAL = 3600

if __name__ == "__main__":
    print("Starting App...")
    app = App(USAGE_THRESHOLD)

    while True:
        try:
            app.updateUsersData()
            app.checkUsageAndNotify()
        except Exception as error:
            print(error)

        time.sleep(TIME_INTERVAL)