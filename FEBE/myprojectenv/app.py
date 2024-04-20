import json
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from modules.recomendation import recommend_job 

app = Flask(__name__)

CORS(app)

@app.route('/')
def serve_home():
    return send_from_directory('./jobbuddy/out', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('./jobbuddy/out', path)

@app.route('/api/employees', methods=['GET'])
def get_employees():
   # print(recommend_job())
   return jsonify({ 'id': 1, 'name': 'Ashley' })

if __name__ == '__main__':
   app.run(port=5000)
