from flask import Flask, render_template, request, jsonify, Response
from pymongo import MongoClient

app = Flask(__name__)
uri = "mongodb+srv://firstData:firstdata10@cluster0-tvr7l.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.batdongsanRaw

# HOME ===================================================
@app.route('/')
def index():
    return render_template('index.html')

# ==============================================================================================
if __name__ == '__main__': app.run(debug=True)