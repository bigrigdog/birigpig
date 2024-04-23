import librosa
import numpy as np
from sklearn.preprocessing import StandardScaler

def extract_features(audio_path):
    """Extract audio features including MFCCs, Chroma, and Mel-Spectrogram."""
    y, sr = librosa.load(audio_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    mel = librosa.feature.melspectrogram(y=y, sr=sr)
    
    features = np.hstack((np.mean(mfcc, axis=1), np.mean(chroma, axis=1), np.mean(mel, axis=1)))
    return features

def preprocess_data(features):
    """Scale features using StandardScaler."""
    scaler = StandardScaler()
    return scaler.fit_transform(features.reshape(1, -1))