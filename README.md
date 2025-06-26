# PneuScan: Pneumonia Detection Web App

PneuScan is a full-stack web application for detecting pneumonia from chest X-ray images using a deep learning model. The project features a Flask backend (API), a React frontend, and a Jupyter notebook for model training and evaluation.

## Features
- Upload chest X-ray images and get instant predictions (Normal or Pneumonia)
- View a history of previous predictions and images
- Clear prediction history with one click
- Modern, responsive UI (React)
- Model training and evaluation notebook included

## Project Structure
```
PneuScan/
├── deploy_app/         # Flask backend
│   ├── app.py
│   ├── requirements.txt
│   ├── move_model.py
│   ├── best_pneumonia_model.h5   # Trained MobileNetV2 model (NEW)
│   ├── templates/
│   └── static/
├── frontend/           # React frontend
│   ├── package.json
│   ├── public/
│   └── src/
├── Pneumonia_Detection_using_CNN.ipynb  # (Legacy) Model notebook
├── Pneumonia_Detection_mobilenetv2.ipynb  # MobileNetV2 notebook (NEW)
├── .gitignore
└── README.md
```

## Setup Instructions

### 1. Backend (Flask)
1. Go to the `deploy_app` folder:
   ```sh
   cd deploy_app
   pip install -r requirements.txt
   ```
2. Place your trained model file as `best_pneumonia_model.h5` in this folder (if not tracked with Git LFS, download or copy it here).
3. Start the backend:
   ```sh
   python app.py
   ```
   The backend will run at [https://pneuscan-1.onrender.com](https://pneuscan-1.onrender.com)

### 2. Frontend (React)
1. Go to the `frontend` folder:
   ```sh
   cd ../frontend
   npm install
   npm start
   ```
2. The app will open at [https://pneu-scan-two.vercel.app/](https://pneu-scan-two.vercel.app/)

### 3. Model Notebook
- The notebook `Pneumonia_Detection_using_CNN.ipynb` contains the model training and evaluation code. You can run it in Jupyter or VS Code.
- **Note:** The raw dataset and large model files are not included in this repo. Please download them separately if needed.

## MobileNetV2 Lightweight Model (NEW)

This project now uses a lightweight MobileNetV2-based model for pneumonia detection, making it suitable for cloud deployment and fast inference.

- **Notebook:** `Pneumonia_Detection_mobilenetv2.ipynb` contains the full workflow for training, evaluating, and saving the MobileNetV2 model.
- **Model File:** The trained model is saved as `best_pneumonia_model.h5` and used by the backend for predictions.
- **Advantages:**
  - Much smaller and faster than a custom CNN
  - Pretrained on ImageNet, then fine-tuned on the pneumonia dataset
  - Lower memory usage, ideal for free-tier cloud services

### How to Use the MobileNetV2 Model
1. Open and run the notebook `Pneumonia_Detection_mobilenetv2.ipynb` to train or retrain the model.
2. After training, ensure `best_pneumonia_model.h5` is present in the `deploy_app` folder.
3. The backend will automatically use this model for predictions.

### Evaluation
- The notebook includes code to evaluate the model on validation data and print accuracy, precision, recall, F1 score, and confusion matrix.

## Usage
- Open the web app in your browser.
- Upload a chest X-ray image (JPG/PNG).
- View the prediction and confidence.
- See your prediction history and clear it with the "Clear History" button.

## Deployment
- **Frontend:** Deploy the `frontend` folder to Vercel or Netlify.
- **Backend:** Deploy the `deploy_app` folder to Render, Railway, or Heroku. Make sure the model file is present on the backend server.
- Update API URLs in the frontend to point to your deployed backend.

## Requirements
- Python 3.8+
- Node.js 16+
- Flask, TensorFlow, OpenCV, React, etc. (see `requirements.txt` and `package.json`)

## License
MIT
