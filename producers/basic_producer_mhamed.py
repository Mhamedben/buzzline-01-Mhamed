import os
import random
import time
from dotenv import load_dotenv
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

load_dotenv()

#####################################
# Define Getter Functions for .env Variables
#####################################

def get_message_interval() -> int:
    """
    Fetch message interval from environment or use a default value.
    """
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval

#####################################
# Define global variables
#####################################

# Define some lists for generating custom buzz messages
ADJECTIVES: list = ["incredible", "hilarious", "shocking", "fantastic", "unexpected"]
ACTIONS: list = ["discovered", "watched", "shared", "experienced", "heard"]
TOPICS: list = ["a podcast", "a new trend", "a viral video", "a book", "a challenge"]

#####################################
# Define a function to generate buzz messages
#####################################

def generate_messages():
    """
    Generate a stream of custom buzz messages.
    """
    while True:
        adjective = random.choice(ADJECTIVES)
        action = random.choice(ACTIONS)
        topic = random.choice(TOPICS)
        yield f"I just {action} {topic}! It was {adjective}!"

#####################################
# Define main() function to run this producer.
#####################################

def main() -> None:
    """
    Main entry point for this producer.
    """
    logger.info("START producer...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    # Get message interval
    interval_secs: int = get_message_interval()

    for message in generate_messages():
        logger.info(message)
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END producer.....")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()