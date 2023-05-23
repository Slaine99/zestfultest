# zestfultest# Recipe Ingredient Parser

This is a Flask application that parses recipe ingredients to extract relevant information such as quantity, unit, product, and preparation.

## Setup

1. Install the required Python packages by running `pip install -r requirements.txt`.
2. Make sure you have spaCy language model "en_core_web_sm" installed. If not, run `python -m spacy download en_core_web_sm`.

## Usage

1. Start the Flask server by running `python app.py`.
2. Send a POST request to `http://localhost:5000/parse` with a JSON payload containing the "ingredients" field.
   Example payload: `{"ingredients": "3 large Granny Smith apples"}`
3. The server will respond with a JSON object containing the parsed ingredient information.

## Ingredient Parsing Process

The parsing process consists of the following steps:

1. Tokenization: The ingredient text is tokenized using the spaCy library to separate the text into individual tokens.
2. Preparation Tokens: The tokens are processed to extract any verbs or adverbs that represent the preparation step.
3. Product Tokens: The tokens representing the product (ingredient) are collected, including adjectives and nouns.
4. Extracted Preparation: The collected preparation tokens are joined together to form the preparation step string.
5. Product Processing: The product tokens are joined to form the product text.
6. Quantity Parsing: The quantity tokens are processed using the pint library to parse and extract the quantity value.
7. Unit Mapping: The product text is checked against a predefined unit mapping to identify the appropriate unit.
8. Size Mapping: The product text is checked against a predefined size mapping to identify the appropriate size.
9. Result: The parsed ingredient information, including preparation, product, quantity, and unit, is returned as a JSON object.

Feel free to modify the `unit_mapping` and `size_mapping` dictionaries to add or customize the mappings according to your specific needs.
