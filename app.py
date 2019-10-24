#!flask/bin/python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

db = []

@app.route('/api/database', methods=['GET'])
def get_db():
    return jsonify({'database': db})

@app.route('/api/add', methods=['POST'])
def create_task():
    db.append(request.json)
    return jsonify(request.json), 201

if __name__ == '__main__':
    app.run(debug=True)