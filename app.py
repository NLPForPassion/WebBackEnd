from flask import Flask, render_template, request, jsonify, Response
from pymongo import MongoClient
import dataBaseAPI

app = Flask(__name__)
uri = "mongodb+srv://firstData:firstdata10@cluster0-tvr7l.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.batdongsanRaw

# HOME ===================================================
@app.route('/')
def index():
    return render_template('index.html')

# GET DATABASE NAME ===================================================
@app.route('/getDataBaseURI')
def getDataBaseURI():
    return dataBaseAPI.getDataBaseURI(request.get_json()['name'])

# REGISTER ===============================================  
# @app.route('/user/register', methods=['GET', 'POST'])
# def register():
    # return userAPI.register(request.get_json())

# ==============================================================================================
if __name__ == '__main__': app.run(debug=True)