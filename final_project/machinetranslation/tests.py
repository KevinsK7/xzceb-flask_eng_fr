import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):

    def test_english_to_french_hello(self):
        result = englishToFrench('Hello')
        self.assertEqual(result.lower(), 'bonjour')

    def test_english_to_french_good_morning(self):
        result = englishToFrench('Good morning')
        self.assertEqual(result.lower(), 'bonjour')

    def test_french_to_english_bonjour(self):
        result = frenchToEnglish('Bonjour')
        self.assertEqual(result.capitalize(), 'Hello')

    def test_french_to_english_bonsoir(self):
        result = frenchToEnglish('Bonsoir')
        self.assertEqual(result.capitalize(), 'Good evening')

if __name__ == '__main__':
    unittest.main()
