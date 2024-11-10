import unittest

# Assuming the function and classes below are defined based on the problem descriptions.

from count_substring import count_substring
from stored_number import StoredNumber
from many_stored_numbers import ManyStoredNumbers

# Define the test cases
class TestLokaprofExercises(unittest.TestCase):

    # Test cases for count_substring function
    def test_count_substring(self):
        self.assertEqual(count_substring("bcaaaaatafg", "aaa"), 3)
        self.assertEqual(count_substring("aaaaaa", "aa"), 5)
        self.assertEqual(count_substring("abcabcabc", "abc"), 3)
        self.assertEqual(count_substring("abcdefg", "h"), 0)
        self.assertEqual(count_substring("", "a"), 0)
        self.assertEqual(count_substring("aaa", "aaa"), 1)

    # Test cases for StoredNumber class
    def test_stored_number(self):
        st_num = StoredNumber(5.0)
        self.assertEqual(str(st_num), "the number: 5.0")
        st_num.set_number(3.4)
        self.assertEqual(st_num.get_number(), 3.4)

    # Test cases for ManyStoredNumbers class
    def test_many_stored_numbers(self):
        many_stored = ManyStoredNumbers()
        many_stored.add_stored_number(StoredNumber(4.6))
        self.assertEqual(str(many_stored), "These are the numbers:\nthe number: 4.6")

        many_stored.add_stored_number(StoredNumber(-3))
        self.assertEqual(str(many_stored), "These are the numbers:\nthe number: 4.6\nthe number: -3")

        many_stored.add_stored_number(StoredNumber(9.0))
        self.assertEqual(str(many_stored), "These are the numbers:\nthe number: 4.6\nthe number: -3\nthe number: 9.0")

if __name__ == "__main__":
    unittest.main()
