import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Path dataset relatif ke file ini
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # folder script
data_path = os.path.join(BASE_DIR, "data", "dataset.csv")

# Load dataset
df = pd.read_csv(data_path)

# Pastikan kolom sesuai CSV
X = df[['N', 'P', 'K', 'temperature', 'ph']]
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Simpan model & scaler di folder model/
model_dir = os.path.join(BASE_DIR, "model")
os.makedirs(model_dir, exist_ok=True)
joblib.dump(model, os.path.join(model_dir, 'crop_model.pkl'))
joblib.dump(scaler, os.path.join(model_dir, 'scaler.pkl'))

def predict_crop(N, P, K, temperature, ph):
    """Prediksi tanaman dari parameter tanah."""
    model_path = os.path.join(model_dir, 'crop_model.pkl')
    scaler_path = os.path.join(model_dir, 'scaler.pkl')
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    data = np.array([[N, P, K, temperature, ph]])
    data_scaled = scaler.transform(data)
    return model.predict(data_scaled)[0]