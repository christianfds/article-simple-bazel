import unittest
from datetime import date, datetime
from freezegun import freeze_time

from routines.calculate_daily_metrics.main import calculate_daily_metrics


class TestCalculateDailyMetrics(unittest.TestCase):
    @freeze_time("2022-09-18")
    def test_output_no_value(self):
        self.assertDictEqual(
            {
                "date": date(2022, 9, 18),
                "generated_at": datetime(2022, 9, 18, 0, 0),
                "extremely_complex_aggregation": -376.43,
            },
            calculate_daily_metrics(),
        )

    @freeze_time("2022-09-18")
    def test_output_value_1(self):
        day = date(2022, 10, 10)
        self.assertDictEqual(
            {
                "date": day,
                "generated_at": datetime(2022, 9, 18, 0, 0),
                "extremely_complex_aggregation": -31.98,
            },
            calculate_daily_metrics(day),
        )

    @freeze_time("2022-09-18")
    def test_output_value_2(self):
        day = date(2022, 9, 10)
        self.assertDictEqual(
            {
                "date": day,
                "generated_at": datetime(2022, 9, 18, 0, 0),
                "extremely_complex_aggregation": 244,
            },
            calculate_daily_metrics(day),
        )

    @freeze_time("2022-09-18")
    def test_output_value_3(self):
        day = date(2022, 11, 10)
        self.assertDictEqual(
            {
                "date": day,
                "generated_at": datetime(2022, 9, 18, 0, 0),
                "extremely_complex_aggregation": -0.26,
            },
            calculate_daily_metrics(day),
        )

    @freeze_time("2022-09-18")
    def test_output_value_4(self):
        day = date(2022, 12, 10)
        self.assertDictEqual(
            {
                "date": day,
                "generated_at": datetime(2022, 9, 18, 0, 0),
                "extremely_complex_aggregation": -135.61,
            },
            calculate_daily_metrics(day),
        )


if __name__ == "__main__":
    unittest.main()
