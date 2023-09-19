import sqlite3
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin

def connect_db():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__,template_folder='./frontend/templates',static_folder='./frontend/static')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, supports_credentials=True)

@app.route("/")
@cross_origin(supports_credentials=True)

def index():
    return render_template('index.html')

# def index():
#     conn = connect_db()
#     autoclaves = conn.execute('SELECT * FROM autoclaves').fetchall()
#     conn.close()
#     return autoclaves

if __name__ == '__main__':
    app.run(host='localhost',port=5000)

