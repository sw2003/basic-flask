from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)

@app.route("/test", methods=['GET'])
def helloWorld():
    return "Hello world" 

if __name__ == '__main__':
    app.run(debug=False, port=8000) 