import sys
import unittest
from find_anagrams import string_contains_anagram

class TestAnagrams(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple_true(self):
        self.assertTrue(string_contains_anagram("crowd",
                                                "word"))

    def test_simple_true2(self):
        self.assertTrue(string_contains_anagram("welisten",
                                                "silent"))

    def test_anagram_is_full_string(self):
        self.assertTrue(string_contains_anagram("listen", "silent"))

    def test_same_word(self):
        self.assertTrue(string_contains_anagram("singleword", "singleword"))

    def test_single_word_fail(self):
        self.assertFalse(string_contains_anagram("singleword", "singlword"))

    def test_single_word_fail_length(self):
        self.assertFalse(string_contains_anagram("singleword", "asingleword"))

    def test_punctuation_and_spaces(self):
        self.assertTrue(string_contains_anagram(
                            "Here come dots and lines that helped build America",
                            "The Morse Code"))

    def test_simple_false(self):
        self.assertFalse(string_contains_anagram(
                            "There is no anagram here",
                            "For this word"))


if __name__ == '__main__':
    unittest.main()
