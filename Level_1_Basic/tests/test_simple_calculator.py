import io
import sys
import unittest
from unittest.mock import patch

from Level_1_Basic import simple_calculator


class TestSimpleCalculator(unittest.TestCase):
    def capture_output(self, func, inputs):
        with patch('builtins.input', side_effect=inputs):
            buf = io.StringIO()
            old = sys.stdout
            try:
                sys.stdout = buf
                func()
            finally:
                sys.stdout = old
            return buf.getvalue()

    def test_addition(self):
        out = self.capture_output(simple_calculator.addition, ['2', '3'])
        self.assertIn('The sum is: 5.0', out)

    def test_subtraction(self):
        out = self.capture_output(simple_calculator.subtraction, ['5', '2'])
        self.assertIn('The difference is: 3.0', out)

    def test_multiplication(self):
        out = self.capture_output(simple_calculator.multiplication, ['4', '2'])
        self.assertIn('The product is: 8.0', out)

    def test_division(self):
        out = self.capture_output(simple_calculator.division, ['9', '3'])
        self.assertIn('The quotient is: 3.0', out)

    def test_division_by_zero(self):
        out = self.capture_output(simple_calculator.division, ['9', '0'])
        self.assertIn('Error: Division by zero is not allowed.', out)


if __name__ == '__main__':
    unittest.main()
