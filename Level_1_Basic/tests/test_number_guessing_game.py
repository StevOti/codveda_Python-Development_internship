import io
import sys
import unittest
from unittest.mock import patch

from Level_1_Basic import number_guessing_game


class TestNumberGuessingGame(unittest.TestCase):
    def run_game_with_inputs(self, inputs, secret):
        with patch('Level_1_Basic.number_guessing_game.random.randint', return_value=secret):
            with patch('builtins.input', side_effect=inputs):
                buf = io.StringIO()
                old = sys.stdout
                try:
                    sys.stdout = buf
                    number_guessing_game.number_guessing_game()
                finally:
                    sys.stdout = old
                return buf.getvalue()

    def test_guess_success(self):
        out = self.run_game_with_inputs(['10', '50', '42'], 42)
        self.assertIn("Congratulations!", out)
        self.assertIn('42', out)

    def test_invalid_input_then_success(self):
        out = self.run_game_with_inputs(['abc', '42'], 42)
        self.assertIn('Invalid input', out)
        self.assertIn('Congratulations!', out)


if __name__ == '__main__':
    unittest.main()
