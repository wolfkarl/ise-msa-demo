import requests
import os
from flask import Flask, jsonify
app = Flask(__name__)
port = int(os.environ.get('PORT', 17002))

@app.route("/products/")
def home():
    products = [
        {"name": "Chocolate Chip Cookie", "price": 299},
        {"name": "Vanilla Twizzle Cookie", "price": 349},
    ]

    return products


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)