#coding:utf-8

from multiprocessing import Queue
from flask import Flask, jsonify

app = Flask(__name__)

class Config(object):
    DEBUG = True

app.config.from_object(Config)

def call_script():
    pass

@app.route('/')
def index():
    data='okokok'
    return jsonify(data)


app.run(host='0.0.0.0', port=12122)