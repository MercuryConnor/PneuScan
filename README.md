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
