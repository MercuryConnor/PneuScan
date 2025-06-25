import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

// Use environment variable for backend API URL, fallback to localhost for dev
const API_URL = process.env.REACT_APP_API_URL || 'https://pneuscan-1.onrender.com';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [clearing, setClearing] = useState(false);

  // Fetch history from backend on mount
  useEffect(() => {
    fetchHistory();
    // eslint-disable-next-line
  }, []);

  const fetchHistory = async () => {
    try {
      const res = await axios.get(`${API_URL}/api/history`);
      // Attach image URL for each history item
      setHistory(
        res.data.map(item => ({
          ...item,
          image: `${API_URL}/uploads/${item.filename}`
        }))
      );
    } catch (err) {
      setHistory([]);
    }
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setSelectedFile(file);
    setPrediction(null);
    setError(null);
    if (file) {
      setPreview(URL.createObjectURL(file));
    } else {
      setPreview(null);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selectedFile) return;
    setLoading(true);
    setError(null);
    const formData = new FormData();
    formData.append('file', selectedFile);
    try {
      const res = await axios.post(`${API_URL}/api/predict`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setPrediction(res.data);
      // Refetch history from backend for persistent update
      fetchHistory();
    } catch (err) {
      setError('Prediction failed. Please try again.');
    }
    setLoading(false);
  };

  const handleClearHistory = async () => {
    setClearing(true);
    try {
      await axios.post(`${API_URL}/api/clear_history`);
      fetchHistory();
    } catch (err) {
      // Optionally show an error
    }
    setClearing(false);
  };

  return (
    <div className="container">
      <h1>PneuScan - Pneumonia Detection</h1>
      <form onSubmit={handleSubmit} className="upload-form">
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <button type="submit" disabled={!selectedFile || loading}>
          {loading ? 'Predicting...' : 'Upload & Predict'}
        </button>
      </form>
      {error && <div className="error">{error}</div>}
      {preview && (
        <div className="preview-section">
          <h3>Selected Image:</h3>
          <img src={preview} alt="Preview" className="preview-img" />
        </div>
      )}
      {prediction && (
        <div className="result-section">
          <h3>Prediction Result:</h3>
          <div className={`result-label ${prediction.label === 'PNEUMONIA' ? 'pneumonia' : 'normal'}`}>
            {prediction.label}
          </div>
          <div className="confidence">Confidence: {prediction.confidence}</div>
        </div>
      )}
      <div className="history-section">
        <h3>History</h3>
        <button className="btn-clear" onClick={handleClearHistory} disabled={clearing || history.length === 0} style={{marginBottom: '16px'}}>
          {clearing ? 'Clearing...' : 'Clear History'}
        </button>
        {history.length === 0 && <div>No history yet.</div>}
        {history.length > 0 && (
          <ul className="history-list">
            {history.map((item, idx) => (
              <li key={idx} className="history-item">
                <img src={item.image} alt="History" className="history-img" />
                <div>
                  <span className={`result-label ${item.label === 'PNEUMONIA' ? 'pneumonia' : 'normal'}`}>{item.label}</span>
                  <span className="confidence">({item.confidence})</span>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default App;
