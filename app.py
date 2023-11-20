from src.EndToEnd_DataScience_Project.logger import logging
from src.EndToEnd_DataScience_Project.exception import CustomException
import sys


if __name__ == "__main__":
    # Set up logger for this script
    logging.info("The execution has started")

    try:
        # error
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)

