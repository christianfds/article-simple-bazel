import logging
import random

from datetime import date, datetime
from libs.logging_utils import get_stdout_handler
from libs.complex_calculations import complex_time_series_aggregation

LOGGER = logging.getLogger("calculate_daily_metrics")


def values_for_day(day: date = None) -> list[float]:
    """Generate random values to a given date

    Args:
        day (date, optional): Date to be fetched. Defaults to None.

    Returns:
        list[float]: Values
    """
    LOGGER.info("Fetching values")
    random.seed(day.toordinal())
    return [random.randrange(-5000, 5000) / 100 for _ in range(100)]


def calculate_daily_metrics(day: date = None) -> dict:
    """Fetch metrics related to the given date

    Args:
        day (date, optional): Date to be processed. Defaults to None.

    Returns:
        dict: Metrics dict
    """
    if not day:
        day = date.today()
    LOGGER.info(f"Calculating metrics to day {day}")

    values = values_for_day(day)
    LOGGER.info("Aggregating metrics")
    agg_value = complex_time_series_aggregation(values)

    metrics = {
        "date": day,
        "generated_at": datetime.now(),
        "extremely_complex_aggregation": agg_value,
    }
    return metrics


if __name__ == "__main__":
    LOGGER.addHandler(get_stdout_handler())
    LOGGER.setLevel(logging.INFO)

    print(calculate_daily_metrics())
