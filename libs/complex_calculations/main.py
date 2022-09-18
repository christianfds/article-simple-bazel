def complex_time_series_aggregation(values: list[float] = None) -> float:
    """Performs an extremelly complex aggregation on all values received

    Args:
        values (list[float], optional): List of values. Defaults to None.

    Returns:
        float: Result
    """
    if not values:
        return 0

    result = 0
    for value in values:
        result += float(value)

    return round(result, 4)
