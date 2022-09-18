import logging
import sys


def get_message_format() -> logging.Formatter:
    """Generates the default message format for logging

    Returns:
        logging.Formatter: Message format
    """
    return logging.Formatter("%(asctime)s [%(levelname)s] %(filename)s:%(lineno)s - %(message)s")


def get_stdout_handler() -> logging.Handler:
    """Loggers to stdout

    Returns:
        logging.Handler: Object to be added as a handler
    """
    formatter = get_message_format()

    handler = logging.StreamHandler(sys.stdout)

    handler.setFormatter(formatter)

    return handler
