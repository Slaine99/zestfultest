import unittest
from main import parse_ingredients

class ParseIngredientsTestCase(unittest.TestCase):
    def test_parse_ingredients(self):
        # Test Case 1
        ingredient_text = "1/2 tsp brown sugar"
        expected_output = {
            "preparation": "",
            "product": "brown sugar",
            "quantity": "1/2",
            "unit": "teaspoons"
        }
        self.assertEqual(parse_ingredients(ingredient_text), expected_output)

        # Test Case 2
        ingredient_text = "3 large Granny Smith apples"
        expected_output = {
            "preparation": "",
            "product": "apples",
            "quantity": "3",
            "unit": "large"
        }
        self.assertEqual(parse_ingredients(ingredient_text), expected_output)

        # Test Case 3
        ingredient_text = "2 1/2 tablespoons finely chopped parsley"
        expected_output = {
            "preparation": "finely chopped",
            "product": "parsley",
            "quantity": "2 1/2",
            "unit": "tablespoons"
        }
        self.assertEqual(parse_ingredients(ingredient_text), expected_output)

if __name__ == '__main__':
    unittest.main()
