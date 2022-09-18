import unittest
from apps.nice_messages.main import pick_a_message_for_the_day
from freezegun import freeze_time


class TestNiceMessagesChoice(unittest.TestCase):
    @freeze_time("2022-09-18")
    def test_output_value_single_call(self):
        self.assertEqual(
            "Happiness depends upon ourselves", pick_a_message_for_the_day()
        )

    @freeze_time("2022-09-18")
    def test_output_value_single_multiple_calls(self):
        for i in range(10):
            with self.subTest(i=i):
                self.assertEqual(
                    "Happiness depends upon ourselves", pick_a_message_for_the_day()
                )

    @freeze_time("2022-09-17")
    def test_output_different_value_d_minus_1(self):
        self.assertEqual("Don't give up", pick_a_message_for_the_day())

    @freeze_time("2022-09-19")
    def test_output_different_value_d_plus_1(self):
        self.assertEqual(
            "Happiness depends upon ourselves", pick_a_message_for_the_day()
        )


if __name__ == "__main__":
    unittest.main()
