import logging
from datetime import datetime

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Python app started")

def main():
    logging.info("Running main logic")
    print("Hello from Python microproject")

if __name__ == "__main__":
    main()
    logging.info("Python app finished")
