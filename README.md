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
