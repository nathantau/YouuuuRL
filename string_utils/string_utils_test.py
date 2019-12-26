import unittest
import string_utils

class StringUtilsTest(unittest.TestCase):

    def test_get_6_digit_representation(self):
        # Given
        code = 'abc'
        expected_code = '000abc'

        # When
        actual_code = string_utils.get_6_digit_representation(code)

        # Then
        self.assertEqual(actual_code, expected_code)