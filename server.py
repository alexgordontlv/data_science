from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, !!!!!!!'
