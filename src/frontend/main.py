import requests
import os
import json
from flask import Flask, jsonify
app = Flask(__name__)
port = int(os.environ.get('PORT', 17001))

products_service_url = "localhost:17002"


def get_products():
    products_json = requests.get(f"http://{products_service_url}/products")
    products = json.loads(products_json.text)
    return products

@app.route("/")
def home():
    products = get_products()
    html = ""
    for product in products:
        html += f"<h2>{product['name']}</h2> <span>{product['price'] / 100} EURO</span>"
    return "Hello, this is a Flask Microservice" + html


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)