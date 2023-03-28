import unittest
from factorizations_comb import duval_

class TestDuval(unittest.TestCase):
    def test_empty_input(self):
        s = ""
        expected = []
        self.assertEqual(duval_(s), expected)
        
    def test_single_character_input(self):
        s = "a"
        expected = ["a"]
        self.assertEqual(duval_(s), expected)
    
    def test_two_equal_characters_input(self):
        s = "aa"
        expected = ["a", "a"]
        self.assertEqual(duval_(s), expected)
    
    def test_two_different_characters_input(self):
        s = "ab"
        expected = ["ab"]
        self.assertEqual(duval_(s), expected)
    
    def test_multiple_characters_input(self):
        s = "abacabadabacaba"
        expected = ["abacabad", "abac", "ab", "a"]
        self.assertEqual(duval_(s), expected)
        
    def test_palindrome_input(self):
        s = "racecar"
        expected = ["r", "acecar"]
        self.assertEqual(duval_(s), expected)
        
    def test_long_input(self):
        s = "abracadabra"
        expected = ["abracad", "abr", "a"]
        self.assertEqual(duval_(s), expected)
        
if __name__ == "__main__":
    unittest.main()
