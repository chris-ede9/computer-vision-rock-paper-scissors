from rock_paper_scissors import RockPaperScissors
import unittest

import random

class RockPaperScissorsTestCase(unittest.TestCase):
     # Initialize the scenario for your test
    def setUp(self):
        self.choices = ["Rock", "Paper", "Scissors"]

    def test_get_computer_choice(self):
        expected_value = self.choices
        actual_value = RockPaperScissors.get_computer_choice(self)
        self.assertTrue(actual_value in expected_value)

    def test_get_winner(self):
        expected_value = ["user", "computer", "tie"]
        actual_value = RockPaperScissors.get_winner(self, random.choice(self.choices), random.choice(self.choices))
        self.assertTrue(actual_value in expected_value)

    # Finish 
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)