from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS
import numpy as np
import tensorflow as tf
import os
import cv2
import subprocess
import json
from datetime import datetime
import uuid

# Ensure model file is present by running move_model.py
subprocess.run(['python', os.path.join(os.path.dirname(__file__), 'move_model.py')], check=False)

# Load the trained model
MODEL_PATH = 'best_pneumonia_model.h5'
model = tf.keras.models.load_model(MODEL_PATH)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

IMG_SIZE = 150
HISTORY_FILE = 'history.json'

# Helper to load/save history

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)

# API endpoint for prediction
@app.route('/api/predict', methods=['POST'])
def api_predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    filename = secure_filename(file.filename)
    unique_filename = f"{uuid.uuid4().hex}_{filename}"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    file.save(filepath)
    # Preprocess image
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=(0, -1))
    # Predict
    pred = model.predict(img)[0][0]
    label = 'PNEUMONIA' if pred > 0.5 else 'NORMAL'
    confidence = float(pred) if pred > 0.5 else 1 - float(pred)
    result = {
        'label': label,
        'confidence': f'{confidence*100:.2f}',
        'filename': unique_filename,
        'timestamp': datetime.now().isoformat()
    }
    # Save to history
    history = load_history()
    history.insert(0, result)
    save_history(history[:30])  # Keep only last 30
    return jsonify(result)

# API endpoint for history
@app.route('/api/history', methods=['GET'])
def api_history():
    history = load_history()
    return jsonify(history)

# API endpoint to clear history
@app.route('/api/clear_history', methods=['POST'])
def api_clear_history():
    save_history([])
    return jsonify({'status': 'cleared'})

# Serve uploaded files for React frontend
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# (Optional) Keep the web UI for legacy/manual use
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    filename = None
    error = None
    if request.method == 'POST':
        if 'file' not in request.files:
            error = 'No file part'
            return render_template('index.html', prediction=None, error=error, filename=None)
        file = request.files['file']
        if file.filename == '':
            error = 'No selected file'
            return render_template('index.html', prediction=None, error=error, filename=None)
        if file:
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4().hex}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(filepath)
            # Preprocess image
            img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            img = img.astype('float32') / 255.0
            img = np.expand_dims(img, axis=(0, -1))
            # Predict
            pred = model.predict(img)[0][0]
            label = 'PNEUMONIA' if pred > 0.5 else 'NORMAL'
            confidence = float(pred) if pred > 0.5 else 1 - float(pred)
            prediction = {'label': label, 'confidence': f'{confidence*100:.2f}%'
            }
            return render_template('index.html', prediction=prediction, filename=unique_filename, error=None)
    return render_template('index.html', prediction=prediction, filename=filename, error=None)

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)
