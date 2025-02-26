import logging
import os

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create a file handler
    if not os.path.exists('logs'):
        os.makedirs('logs')
    file_handler = logging.FileHandler(f'logs/{name}.log')
    file_handler.setLevel(logging.INFO)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
