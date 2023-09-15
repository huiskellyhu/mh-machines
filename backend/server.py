from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/")
@cross_origin(supports_credentials=True)

def home():
    return "Hello! main page <h1>HELLO</h1>"

