import requests
import os
import random
from faker import Faker
from flask import Flask, jsonify
app = Flask(__name__)
port = int(os.environ.get('PORT', 80))

fake = Faker()

def fake_post():
    return {
        "id": random.randint(1,100_000),
        "user_id": random.randint(1,3),
        "text": fake.text(),
    }

@app.route("/posts/")
def posts():
    num_posts = 100
    posts = [fake_post() for _ in range(num_posts)]

    return posts


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)