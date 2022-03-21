import unittest
from src.main import set_singular_or_plural_wording

class TestMain(unittest.TestCase):
    plural_wording: str = 'subscribers'
    singular_wording: str = 'subscriber'

    def test_set_single_or_plural_wording(self):
        wording = set_singular_or_plural_wording(0)
        self.assertEqual(self.plural_wording, wording)
        
        wording = set_singular_or_plural_wording(1)
        self.assertEqual(self.singular_wording, wording)

if __name__ == '__main__':
    unittest.main()