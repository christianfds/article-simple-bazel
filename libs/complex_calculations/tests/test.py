import unittest
from libs.complex_calculations import complex_time_series_aggregation


class TestComplexTimeSeriesAggregation(unittest.TestCase):
    def test_output_no_value(self):
        self.assertEqual(0, complex_time_series_aggregation())

    def test_output_empty_value(self):
        self.assertEqual(0, complex_time_series_aggregation([]))

    def test_output_single_value(self):
        self.assertEqual(10.5, complex_time_series_aggregation([10.5]))

    def test_output_multiple_values(self):
        self.assertEqual(510.5, complex_time_series_aggregation([10.5, 500]))

    def test_output_single_negative_value(self):
        self.assertEqual(-10.3, complex_time_series_aggregation([-10.3]))

    def test_output_multiple_negative_values(self):
        self.assertEqual(-489.7, complex_time_series_aggregation([10.3, -500]))

    def test_output_multiple_negative_and_positive_values(self):
        self.assertEqual(-510.3, complex_time_series_aggregation([-10.3, -500]))

    def test_output_invalid_single_value(self):
        with self.assertRaises(ValueError):
            complex_time_series_aggregation(["potato"])

    def test_output_invalid_multiple_values(self):
        with self.assertRaises(ValueError):
            complex_time_series_aggregation([100, "potato"])


if __name__ == "__main__":
    unittest.main()
