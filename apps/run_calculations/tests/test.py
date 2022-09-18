import unittest
from apps.run_calculations.main import fetch_aggregation_results


class TestFetchAggregationResultsChoice(unittest.TestCase):
    def test_output_value(self):
        self.assertEqual(60, fetch_aggregation_results([10, 20, 30]))

    def test_output_no_value(self):
        self.assertEqual(0, fetch_aggregation_results())

    def test_output_empty_value(self):
        self.assertEqual(0, fetch_aggregation_results([]))

    def test_output_multiple_values_1(self):
        self.assertEqual(-6.5, fetch_aggregation_results([-10.5, 4]))

    def test_output_multiple_values_2(self):
        self.assertEqual(-14.5, fetch_aggregation_results([-10.5, -4]))

    def test_output_multiple_invalid_value_1(self):
        self.assertEqual(0, fetch_aggregation_results([None]))

    def test_output_multiple_invalid_value_2(self):
        self.assertEqual(0, fetch_aggregation_results(["potato"]))

    def test_output_multiple_invalid_value_3(self):
        self.assertEqual(0, fetch_aggregation_results([{"potato": "chips"}]))

    def test_output_multiple_invalid_values_1(self):
        self.assertEqual(-10.5, fetch_aggregation_results([-10.5, None]))

    def test_output_multiple_invalid_values_2(self):
        self.assertEqual(-10.5, fetch_aggregation_results([-10.5, "potato"]))

    def test_output_multiple_invalid_values_3(self):
        self.assertEqual(-10.5, fetch_aggregation_results([-10.5, {"potato": "chips"}]))


if __name__ == "__main__":
    unittest.main()
