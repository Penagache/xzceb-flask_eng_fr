import unittest
from machinetranslation import translator

class TestTranslation(unittest.TestCase):
    """
    Class to test the module Translation
    """

    def test_english_to_french(self):
        """test the function english_to_french"""
        self.assertIsNone(translator.english_to_french(None))
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(translator.english_to_french("Bonjour"), "Hello")

    def test_french_to_english(self):
        """test the function french_to_english"""
        self.assertIsNone(translator.french_to_english(None))
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(translator.french_to_english("Hello"), "Bonjour")


if __name__ == "__main__":
    unittest.main()