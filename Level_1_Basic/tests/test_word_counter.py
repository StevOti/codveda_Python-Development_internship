import os
import tempfile
import unittest

from Level_1_Basic.word_counter import count_words_in_file


class TestWordCounter(unittest.TestCase):
    def test_count_words_in_file(self):
        content = "Hello world\nThis is a test file."
        with tempfile.NamedTemporaryFile('w', delete=False) as tf:
            tf.write(content)
            path = tf.name

        try:
            result = count_words_in_file(path)
            # "Hello world" + "This is a test file." -> 7 words
            self.assertEqual(result, 7)
        finally:
            os.remove(path)

    def test_file_not_found(self):
        result = count_words_in_file('non_existent_file_12345.txt')
        self.assertIsInstance(result, str)
        self.assertIn('not found', result.lower())


if __name__ == '__main__':
    unittest.main()
