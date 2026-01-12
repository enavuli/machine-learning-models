import os
import json
from typing import Dict, List
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_config(file_path: str) -> Dict:
    with open(file_path, 'r') as file:
        return json.load(file)

def split_data(data: pd.DataFrame, target: str, test_size: float = 0.2, random_state: int = 42) -> tuple:
    X = data.drop(target, axis=1)
    y = data[target]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def scale_data(X_train: pd.DataFrame, X_test: pd.DataFrame) -> tuple:
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled

def save_model(model, file_path: str) -> None:
    # check if directory exists
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    # save model
    with open(file_path, 'wb') as file:
        import pickle
        pickle.dump(model, file)

def load_model(file_path: str):
    with open(file_path, 'rb') as file:
        import pickle
        return pickle.load(file)

def evaluate_model(y_test: np.ndarray, y_pred: np.ndarray) -> Dict:
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    return {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1': f1_score(y_test, y_pred)
    }