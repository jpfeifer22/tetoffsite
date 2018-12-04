
from flask import Flask 
import json
import os
import sys

app = Flask(__name__)

f = open("talos.out.raw", "r")

data = f.read()

@app.route("/")
def hello():
    #print "hi"
    #a=5
    #b=6
    #return jsonify(result=a + b)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
