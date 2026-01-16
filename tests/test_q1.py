"""Tests for Lab 0 Question 1"""

import sys
sys.path.append(".")
import unittest
from src.q1 import is_palindrome


class testispalindrome(unittest.TestCase):


    def test_simple_palindrome(self) -> None:
        self.assertTrue(is_palindrome("racecar"))

    def test_simple_not_palindrome(self) -> None:
        self.assertFalse(is_palindrome("This is not a palindrome"))

    def test_case_insensitive(self) -> None:
        self.assertTrue(is_palindrome("RaceCar"))

    def test_with_spaces(self) -> None:
        self.assertTrue(is_palindrome("sit on a potato pan otis"))

    def test_empty_string(self) -> None:
        self.assertTrue(is_palindrome(""))


   



