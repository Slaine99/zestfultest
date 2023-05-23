import spacy
import pint
from flask import Flask, request, jsonify

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")
ureg = pint.UnitRegistry()

unit_mapping = {
    "tablespoons": ["tablespoon", "tbsp"],
    "teaspoons": ["teaspoon", "tsp"],
    "cups": ["cup"],
}

size_mapping = {
    "large": ["large"],
    "medium": ["medium"],
    "small": ["small"],
}

def parse_ingredients(ingredient_text):
    parsed_results = {
        "preparation": "",
        "product": "",
        "quantity": "",
        "unit": "",
    }

    doc = nlp(ingredient_text)

    preparation_tokens = []
    adverb_tokens = []
    product_tokens = []

    for token in doc:
        if token.pos_ == "NUM":
            parsed_results["quantity"] += token.text + " "
        elif token.pos_ == "VERB":
            if adverb_tokens:
                adverb_prep = " ".join([adv.text for adv in adverb_tokens])
                preparation_tokens.append(adverb_prep)
                adverb_tokens = []
            preparation_tokens.append(token.text)
        elif token.pos_ == "ADV":
            adverb_tokens.append(token)
        elif token.pos_ == "ADJ":
            product_tokens.append(token.text)
        elif token.pos_ == "NOUN":
            product_tokens.append(token.text)

    parsed_results["preparation"] = " ".join(preparation_tokens).strip()

    # Process the product tokens to separate unit and product
    product_text = " ".join(product_tokens)
    quantity = ureg.parse_expression(parsed_results["quantity"].strip())

    # Check for unit mapping
    for unit, aliases in unit_mapping.items():
        if any(alias in product_text for alias in aliases):
            parsed_results["unit"] = unit
            product_text = product_text.replace(unit, "").strip()
            for alias in aliases:
                product_text = product_text.replace(alias, "").strip()
            break

    # Check for size mapping
    for size, aliases in size_mapping.items():
        if any(alias in product_text for alias in aliases):
            parsed_results["unit"] = size
            product_text = product_text.replace(size, "").strip()
            for alias in aliases:
                product_text = product_text.replace(alias, "").strip()
            break

    parsed_results["product"] = product_text

    # Remove leading/trailing whitespace from quantity field
    parsed_results["quantity"] = parsed_results["quantity"].strip()

    return parsed_results


@app.route("/parse", methods=["POST"])
def parse_ingredients_route():
    data = request.json
    ingredient_text = data.get("ingredients", "")

    parsed_ingredients = parse_ingredients(ingredient_text)

    return jsonify(parsed_ingredients)


if __name__ == "__main__":
    app.run(debug=True)
