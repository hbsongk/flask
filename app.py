from flask import Flask, render_template, request, jsonify
from pymango import MongoClient
from datetime import datetime, timedelta

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.bird_comming

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)