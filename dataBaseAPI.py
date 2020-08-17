from flask import Flask, render_template, request, jsonify, Response
from pymongo import MongoClient
from bson import ObjectId
import resultCF

uris = ['mongodb+srv://firstData:<password>@cluster-iukdn.mongodb.net/<dbname>?retryWrites=true&w=majority']

# ==============================================================================================
def getURIIndex(dataBaseName):
    if dataBaseName=='dictionaryVN':
        return 0
    return -1

# ==============================================================================================
def getDataBaseURI(dataBaseName):
    try:
        id = getURIIndex(dataBaseName)
        res = {}
        if id==-1:
            return jsonify(resultCF.cf_res(res,'100','null'))
        return jsonify(resultCF.cf_res(res, '1',uris[id]))
    except:
        return jsonify(resultCF.cf_res(res,'0','null'))
    