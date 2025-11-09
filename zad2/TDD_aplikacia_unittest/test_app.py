import unittest
from app import (
    walidacjaemail, area, filtrsort, konwertacja, palindrome
)

class TestWalidacjaEmail(unittest.TestCase):
    def test_valid_emails(self):
        for e in ["a@b.co", "jan.kowalski@example.com", "x_y-1@sub.domain.org"]:
            with self.subTest(e=e):
                self.assertTrue(walidacjaemail(e))

    def test_invalid_emails(self):
        for e in ["", "a@b", "a b@c.com", "no-at.com", "a@b.", "@b.com"]:
            with self.subTest(e=e):
                self.assertFalse(walidacjaemail(e))

    def test_none_returns_false(self):
        self.assertFalse(walidacjaemail(None))

class TestArea(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(area(3, 4), 12)
        self.assertEqual(area(0, 5), 0)

    def test_float(self):
        self.assertAlmostEqual(area(2.5, 4.0), 10.0, places=6)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            area(-1, 2)
        with self.assertRaises(ValueError):
            area(1, -2)

class TestFiltrSort(unittest.TestCase):
    def test_default_threshold(self):
        self.assertEqual(filtrsort([3, -1, 2, 0]), [2, 3])

    def test_custom_threshold(self):
        self.assertEqual(filtrsort([10, 5, 1, 7], threshold=6), [7, 10])

    def test_all_filtered_out(self):
        self.assertEqual(filtrsort([-5, -1, 0], threshold=0), [])

class TestKonwertacja(unittest.TestCase):
    def test_default_formats(self):
        self.assertEqual(konwertacja("25-12-2024"), "2024/12/25")

    def test_custom_formats(self):
        self.assertEqual(konwertacja("2024.01.02", "%Y.%m.%d", "%d/%m/%Y"), "02/01/2024")

    def test_invalid_input_raises(self):
        with self.assertRaises(ValueError):
            konwertacja("31-02-2024")

class TestPalindrome(unittest.TestCase):
    def test_true_cases(self):
        for s in ["Kajak", "Kobyła ma mały bok", "12321", "A man, a plan, a canal: Panama!"]:
            with self.subTest(s=s):
                self.assertTrue(palindrome(s))

    def test_false_cases(self):
        for s in ["Test", "Ala ma kota", "123210"]:
            with self.subTest(s=s):
                self.assertFalse(palindrome(s))

    def test_empty_is_palindrome(self):
        self.assertTrue(palindrome(""))

if __name__ == "__main__":
    unittest.main()
