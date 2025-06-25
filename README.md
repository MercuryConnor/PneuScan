<<<<<<< HEAD
# PneuScan: Pneumonia Detection Web App

A full-stack web application for pneumonia detection from chest X-ray images using a deep learning model. Built with Flask (backend/API), React (frontend), and Keras/TensorFlow (model).

## Features
- Upload X-ray images and get instant predictions (Normal or Pneumonia)
- View a history of previous predictions and images
- Clear history with one click
- Modern, responsive UI (React)

## Project Structure
```
PneuScan/
├── deploy_app/         # Flask backend
│   ├── app.py
│   ├── requirements.txt
│   ├── move_model.py
│   ├── templates/
│   └── static/
├── frontend/           # React frontend
│   ├── package.json
│   ├── public/
│   └── src/
├── Pneumonia_Detection_using_CNN.ipynb  # Model notebook
├── .gitignore
└── README.md
```

## Setup Instructions

### Backend (Flask)
1. Go to `deploy_app` folder:
   ```sh
   cd deploy_app
   pip install -r requirements.txt
   ```
2. Place your trained model file as `best_pneumonia_model.h5` in this folder.
3. Start the backend:
   ```sh
   python app.py
   ```

### Frontend (React)
1. Go to `frontend` folder:
   ```sh
   cd ../frontend
   npm install
   npm start
   ```
2. The app will open at [http://localhost:3000](http://localhost:3000)

### Model Notebook
- The notebook `Pneumonia_Detection_using_CNN.ipynb` contains the model training and evaluation code. (No raw data or large model files are included in this repo.)

## Deployment
- Deploy the backend (Flask) to Render, Railway, or Heroku.
- Deploy the frontend (React) to Vercel or Netlify.
- Update API URLs in the frontend to point to your deployed backend.

## License
MIT
=======
# PneuScan: AI-Powered X-Ray Analysis

PneuScan is an AI-powered medical imaging solution designed to classify pneumonia from chest X-ray images using deep learning. The project leverages Convolutional Neural Networks (CNNs) to achieve high accuracy and is deployed as a REST API for seamless integration into healthcare systems.

---

## 🚀 **Features**
- **Pneumonia Classification**: Accurately classify chest X-ray images as "Pneumonia" or "Normal."
- **Data Augmentation**: Handle class imbalance and improve model robustness using advanced augmentation techniques.
- **REST API**: Deploy the model as a Flask-based REST API for real-time predictions.
- **Performance Metrics**: Achieves **85% accuracy** with detailed evaluation using precision, recall, and F1-score.

---

## 📂 **Dataset**
The project uses the [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) dataset from Kaggle, containing:
- **5,856 X-ray images** (train, test, and validation sets).
- Two classes: **Pneumonia** and **Normal**.

---

## 🛠️ **Technologies Used**
- **Programming Language**: Python
- **Deep Learning Frameworks**: TensorFlow, Keras
- **Computer Vision**: OpenCV
- **Data Augmentation**: ImageDataGenerator
- **Model Evaluation**: Scikit-learn
- **Deployment**: Flask, REST API
- **Visualization**: Matplotlib, Seaborn
- **Version Control**: GitHub

---

## 📊 **Performance Metrics**
- **Accuracy**: 85%
- **Precision**: 0.87
- **Recall**: 0.85
- **F1-Score**: 0.86

---

## 🚀 **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pneuscan.git
   cd pneuscan
>>>>>>> 86e6b8381702a8fb8bf5c2b3054d48bac8a526ea
