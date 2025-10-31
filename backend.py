from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # <-- This line allows all origins

@app.route('/news.categories.get')
def get_categories():
    data = {
        "title": "List of Categories",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "categories": [
            {"id": 1, "name": "Sports"},
            {"id": 2, "name": "Politics"},
            {"id": 3, "name": "Education"}
        ]
    }
    return jsonify(data)

@app.route('/')
def index():
    return 'Welcome to Flask Backend!'

if __name__ == "__main__":
    app.run(port=8080)
