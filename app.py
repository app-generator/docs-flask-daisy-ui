from flask import Flask, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/hello')
def hello():
    return {'message': 'Hello from Flask!'}

# Serve frontend in production
@app.route('/')
def serve_frontend():
    return send_from_directory('frontend/dist', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('frontend/dist', path)

if __name__ == '__main__':
    app.run(debug=True)