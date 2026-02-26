import schedule
import time
from services import call_instacart_api


if __name__ == "__main__":
    schedule.every().friday.at("19:30").do(call_instacart_api)

    while True:
        schedule.run_pending()
        time.sleep(1)