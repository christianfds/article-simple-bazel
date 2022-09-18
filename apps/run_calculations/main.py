import logging

from flask import Flask, jsonify, request

from libs.logging_utils import get_stdout_handler
from libs.complex_calculations import complex_time_series_aggregation

LOGGER = logging.getLogger("run_calculations")

app = Flask(__name__)


def isfloat(value) -> bool:
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def fetch_aggregation_results(values: list[float] = None) -> float:
    """Filters invalid values and calculates the aggregation

    Args:
        values (list[float], optional): List of values to be aggregated. Defaults to None.

    Returns:
        float: Aggregation result.
    """
    if not values:
        values = []

    values = filter(lambda v: isfloat(v), values)

    final_value = complex_time_series_aggregation(values)

    return final_value


@app.route("/")
def aggregate_time_series() -> dict:
    values = request.args.getlist("values", type=float)
    LOGGER.info(f"Request with args: {values}")

    final_value = fetch_aggregation_results(values)
    return jsonify({"calculated_value": final_value})


if __name__ == "__main__":
    LOGGER.addHandler(get_stdout_handler())
    LOGGER.setLevel(logging.DEBUG)

    app.run(debug=True)
