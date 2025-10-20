# main.py
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from model import NeuralNet
from dataset import MyDataset

# Load the dataset
df = pd.read_csv('data.csv')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['features'], df['target'], test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create a dataset and data loader for the training data
dataset = MyDataset(X_train_scaled, y_train)
train_loader = DataLoader(dataset, batch_size=32, shuffle=True)

# Create a dataset and data loader for the testing data
dataset = MyDataset(X_test_scaled, y_test)
test_loader = DataLoader(dataset, batch_size=32, shuffle=False)

# Create a neural network model
model = NeuralNet(input_dim=X_train.shape[1], hidden_dim=128, output_dim=1)

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the model
for epoch in range(100):
    for i, (inputs, labels) in enumerate(train_loader):
        # Zero the gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        # Backward pass and optimization
        loss.backward()
        optimizer.step()

        if (i+1) % 100 == 0:
            print(f'Epoch: {epoch+1}, Batch: {i+1}, Loss: {loss.item()}')

# Test the model
model.eval()
with torch.no_grad():
    total = 0
    correct = 0
    for inputs, labels in test_loader:
        outputs = model(inputs)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = correct / total
print(f'Test accuracy: {accuracy:.2f}')