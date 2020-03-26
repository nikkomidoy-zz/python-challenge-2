import unittest

from lottery import spin_lottery


class LotteryTest(unittest.TestCase):
    def test_selected_numbers_only_10_by_default(self):
        self.assertEqual(
            len(spin_lottery()), 10
        )

    def test_selected_numbers_are_integers(self):
        selected_numbers = spin_lottery()
        self.assertTrue(
            all(isinstance(number, int) for number in selected_numbers)
        )

    def test_selected_numbers_are_within_1_to_50(self):
        selected_numbers = spin_lottery()
        self.assertTrue(
            all(number <= 50 and number >=1 for number in selected_numbers)
        )

    def test_custom_define_number_balls_and_picks(self):
        number_of_balls = 40
        number_of_picks = 8
        selected_numbers = spin_lottery(number_of_balls, number_of_picks)
        self.assertEqual(
            len(selected_numbers), number_of_picks
        )
        self.assertTrue(
            all(number <= number_of_balls and number >=1 for number in selected_numbers)
        )


if __name__ == '__main__':
    unittest.main()
