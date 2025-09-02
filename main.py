import time
from classes.app import App

TIME_INTERVAL = 3600

if __name__ == "__main__":
    app = App()

    while True:
        try:
            app.updateUsersData()
            app.checkUsageAndNotify()
        except Exception as error:
            print(error)

        time.sleep(TIME_INTERVAL)