import random
import datetime
import logging

from flask import Flask, jsonify

from libs.logging_utils import get_stdout_handler

LOGGER = logging.getLogger("nice_messages")

app = Flask(__name__)

MESSAGES = [
    "Believe in yourself",
    "Don't give up",
    "Hold on",
    "Stay positive",
    "Enjoy life",
    "Enjoy the little things",
    "You are awesome",
    "Friends are relatives you make for yourself",
    "Happiness depends upon ourselves",
]


def pick_a_message_for_the_day() -> str:
    """Returns a nice message for each day

    Returns:
        str: Message
    """
    current_date = datetime.date.today()
    LOGGER.info(f"Selecting a nice message on day {current_date}")
    random.seed(current_date.toordinal())

    return random.choice(MESSAGES)


@app.route("/")
def get_daily_message() -> dict:
    """Endpoint that returns nice messages

    Returns:
        dict: JSON with a daily nice message
    """
    message = pick_a_message_for_the_day()

    return jsonify({"daily_message": message})


if __name__ == "__main__":
    LOGGER.addHandler(get_stdout_handler())
    LOGGER.setLevel(logging.DEBUG)

    app.run(debug=True)
