import requests
import os
import json
import random
import logging
import pathlib
from flask import Flask, jsonify
app = Flask(__name__)
port = int(os.environ.get('PORT', 17001))

products_service_url = "http://src-products:17002"

service_id = random.randrange(1, 100000)
pod = pathlib.Path("/etc/hostname").read_text()


def get_products():
    products = {}
    try:
        products_json = requests.get(f"{products_service_url}/products")
        products = json.loads(products_json.text)
    except requests.exceptions.ConnectionError as e:
        logging.warning("error accessing products aah")
        logging.warning(e)
    return products

@app.route("/")
def home():
    products = get_products()
    html = f"<h1>Great Service, id={pod}</h1>\n"
    for product in products:
        html += f"<h2>{product['name']}</h2> <span>{product['price'] / 100} EURO</span>"
    return "Hello, this is a Flask Microservice" + html


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)