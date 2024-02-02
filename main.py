# app.py
from flask import Flask, request
import os
import subprocess
import pickle
import json

app = Flask(__name__)

@app.route('/exec', methods=['GET'])
def exec_command():
    # Direkte Ausführung von Benutzereingaben ohne Validierung
    user_input = request.args.get('cmd')
    command = user_input.replace(';', '').replace('&', '')
    subprocess.call(command)
    return "Kommando ausgeführt\n"

@app.route('/upload', methods=['POST'])
def upload_file():
    # Unsichere Deserialisierung von Benutzereingaben
    file = request.files['file'].read()
    data = json.loads(file)
    return "Datei hochgeladen\n"

@app.route('/run', methods=['POST'])
def run_command():
    return "Run route disabled\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
