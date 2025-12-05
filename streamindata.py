from flask import Flask,jsonify
from loaddata import loaddata
import json
app = Flask(__name__)

@app.route("/getreviews",methods=['GET'])
def getreviews():
    return jsonify(loaddata())