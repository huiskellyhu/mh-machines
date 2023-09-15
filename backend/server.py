from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, supports_credentials=True)

@app.route("/")
@cross_origin(supports_credentials=True)

def home():
    return "Hello! main page <h1>HELLO</h1>"

