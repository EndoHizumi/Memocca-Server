from flask import Flask, request, redirect, jsonify
from .models import board, sticky, user

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
