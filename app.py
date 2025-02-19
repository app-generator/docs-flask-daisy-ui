from flask import Flask, send_from_directory
from flask import render_template, request, redirect, url_for
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/api/hello')
def hello():
    return {'message': 'Hello from Flask!'}

# Serve frontend in production
@app.route('/')
def index():

    context = {
        'timestamp': datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
    }
    
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True)