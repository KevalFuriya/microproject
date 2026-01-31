import logging
import time
import random

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Application started")

for i in range(5):
    num = random.randint(1, 100)
    if num % 2 == 0:
        logging.info(f"{num} is even")
    else:
        logging.error(f"{num} is odd")
    time.sleep(2)

logging.info("Application finished")
